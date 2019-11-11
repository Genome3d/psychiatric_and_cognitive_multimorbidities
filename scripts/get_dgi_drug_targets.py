#! /usr/bin/env python

import sys
import argparse
import json
import requests
import pandas as pd
import csv
import os


def usage():
    print "Usage Examples:"
    print "python python_example.py --help"
    print "python python_example.py --genes='FLT3'"
    print "python python_example.py --genes='FLT3,EGFR,KRAS'"
    print "python python_example.py --genes='FLT3,EGFR' --interaction_sources='TALC,TEND'"
    print "python python_example.py --genes='FLT3,EGFR' --gene_categories='KINASE'"
    print "python python_example.py --genes='FLT3,EGFR' --interaction_types='inhibitor'"
    print "python python_example.py --genes='FLT3,EGFR' --source_trust_levels='Expert curated'"
    print "python python_example.py --genes='FLT3,EGFR' --antineoplastic_only"
    print "python python_example.py --genes='FLT3,EGFR,KRAS' --interaction_sources='TALC,TEND,MyCancerGenome' --gene_categories='KINASE' --interaction_types='inhibitor' --antineoplastic_only"
    sys.exit(0)


def parse_args():
    parser = argparse.ArgumentParser(description="A Python example for using the DGIdb API",
                                     epilog="For complete API documentation refer to http://dgidb.org/api")
    parser.add_argument(
        "-g", "--genes", required=True,
        help="The significant_eqtls.txt file or a txt file containing a list of gene symbols(REQUIRED). Use official Entrez symbols for best results", dest="genes")
    parser.add_argument(
        "-o", "--output_dir", required=True,
        help="Filepath of directory to write results.")
    parser.add_argument("-is", "--interaction_sources",
                        help="Limit results to those from particular data sources. e.g. 'DrugBank', 'PharmGKB', 'TALC', 'TEND', 'TTD', 'MyCancerGenome')", dest="interaction_sources")
    parser.add_argument("-it", "--interaction_types",
                        help="Limit results to interactions with drugs that have a particular mechanism of action. e.g. 'inhibitor', 'antibody', etc", dest="interaction_types")
    parser.add_argument("-gc", "--gene_categories",
                        help="Limit results to genes with a particular druggable gene type. e.g. 'KINASE', 'ION CHANNEL', etc", dest="gene_categories")
    parser.add_argument("-stl", "--source_trust_levels",
                        help="Limit results based on trust level of the interaction source. e.g. 'Expert curated' or 'Non-curated", dest="source_trust_levels")
    parser.add_argument("-ano", "--antineoplastic_only", help="Limit results to anti-cancer drugs only",
                        dest="antineoplastic_only", action='store_true')
    parser.add_argument("-u", "--usage", help="Usage examples",
                        dest="usage", action='store_true')
    return parser.parse_args()


def parse_inputs(filepath):
    print('Parsing input file')
    gene_list = ' ,'
    try:  # File is significant_eqtls.txt from CoDeS3D
        gene_file = open(filepath)
        gene_df = pd.read_csv(gene_file, sep='\t')
        gene_list = gene_list.join(gene_df['Gene_Name'].unique())
    except:
        gene_df = set()
        with open(filepath, 'r') as gene_file:
            reader = csv.reader(gene_file, delimiter='\t')
            for row in reader:
                gene_df.add(row[0])
        gene_list = gene_list.join(gene_df)
    return gene_list


class DGIAPI:
    'API Example class for DGI API.'
    domain = 'http://dgidb.org/'
    api_path = '/api/v1/interactions.json'

    def __init__(self, args):
        self.genes = parse_inputs(args.genes)
        self.interaction_sources = args.interaction_sources
        self.interaction_types = args.interaction_types
        self.gene_categories = args.gene_categories
        self.source_trust_levels = args.source_trust_levels
        self.antineoplastic_only = args.antineoplastic_only
        self.output_dir = args.output_dir
        self.output_filepath = os.path.join(
            self.output_dir, 'dgi_druggable_genes.txt')

    def run_workflow(self):
        self.create_request()
        self.post_request()
        self.print_response()

    def create_request(self):
        self.request = "http://dgidb.org/api/v1/interactions.json?genes=FLT1&drug_types=antineoplastic&interaction_sources=TALC"
        self.payload = {}
        if(self.genes):
            self.payload['genes'] = self.genes
        if(self.interaction_sources):
            self.payload['interaction_sources'] = self.interaction_sources
        if(self.gene_categories):
            self.payload['gene_categories'] = self.gene_categories
        if(self.interaction_types):
            self.payload['interaction_types'] = self.interaction_types
        if(self.source_trust_levels):
            self.payload['source_trust_levels'] = self.source_trust_levels
        if(self.antineoplastic_only):
            self.payload['drug_types'] = 'antineoplastic'

    def post_request(self):
        print('Querying DGI database...')
        self.request = DGIAPI.domain + DGIAPI.api_path
        self.response = requests.post(self.request, data=self.payload)

    def print_response(self):
        print('Writing results...')
        response = json.loads(self.response.content)
        matches = response['matchedTerms']
        if(matches):
            # print "gene_name\tdrug_name\tinteraction_type\tsource\tgene_categories"
            output_file = open(self.output_filepath, 'w')
            writer = csv.writer(output_file, delimiter='\t')
            writer.writerow(['Gene_Name', 'Drug_Name', 'Interaction_Type',
                             'Source', 'Gene_Categories'])
        for match in matches:
            gene = match['geneName']
            categories = match['geneCategories']
            categories.sort()
            joined_categories = ",".join(categories)
            for interaction in match['interactions']:
                source = interaction['source']
                drug = interaction['drugName']
                interaction_type = interaction['interactionType']
                #gene + "\t" + drug + "\t" + interaction_type + "\t" + source \
                #    + "\t" + joined_categories.lower()
                writer.writerow([gene, drug.encode('utf-8'), interaction_type, source,
                                 joined_categories.capitalize()])
        for unmatched in response['unmatchedTerms']:
            print "Unmatched search term: " + unmatched['searchTerm']
            print "Possible suggestions: " + ",".join(unmatched['suggestions'])
        if(os.path.isfile(self.output_filepath)):
            output_file.close()
        print('Done.')


if __name__ == '__main__':
    args = parse_args()
    if(not args.genes or args.usage):
        usage()
    da = DGIAPI(args)
    da.run_workflow()
