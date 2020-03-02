#/mnt/3dgenome/programs/R/R-3.6.0/bin/R
#options(width=as.integer(system("stty -a | head -n 1 | awk '{print $7}' | sed 's/;//'", intern=T)))
setwd("/Volumes/resmed201800011-foffa/Archive/projects/P1_ND_and_Cogntiion/pLI")

pacman::p_load(dplyr, ggplot2, RColorBrewer, "scales", ggrepel, ggbeeswarm, ggalt,
               magrittr, tidybayes, tidyr)

table_in <- read.table(file=gzfile('gnomad.v2.1.1.lof_metrics.by_gene.txt.bgz','rt'),
                       header = TRUE, sep="\t")
table_in_pheno <- read.table(file="/Volumes/resmed201800011-foffa/Archive/projects/P1_ND_and_Cogntiion/pLI/ASD_significant_eqtls.txt",
                               header = TRUE, sep="\t")
table_in_pheno_cistrans <- table_in_pheno %>% 
	mutate(cistrans=ifelse(SNP_Chromosome==Gene_Chromosome & cis_SNP.gene_interaction=="True", "cis", 
	                       ifelse(SNP_Chromosome==Gene_Chromosome & cis_SNP.gene_interaction=="False", "trans_intra", "trans_inter")))

Gene_list <- table_in_pheno_cistrans %>% 
	select(Gene_Name, cistrans) %>% 
	arrange(Gene_Name) %>% 
	distinct() %>% 
	rename(gene = Gene_Name) 

table_in_pheno <- table_in %>% 
	select(gene, pLI) %>% 
	mutate(intolerant=ifelse(pLI>=0.9, "Intolerant", "Tolerant")) %>% #dichotomize the continuous variable - 0.9 and above is the threshold for "LoF intolerant"
	mutate(intolerant=ifelse(is.na(intolerant),"nopli",intolerant)) %>% #change NA to a label on the plot I can control
	full_join(Gene_list) %>% #merge sigeqtl and gnomad files, merge by gene name
	mutate(cistrans=ifelse(is.na(cistrans),"noeQTL",cistrans)) %>% #change NA to a label on the plot I can control
	mutate(cistrans=factor(cistrans, levels=c("noeQTL","cis","trans_intra","trans_inter"))) #This sets the order of the levels on the plots below
table_in_pheno2 <- table_in_pheno %>% #this part seems necessary as there are still some NAs after the first batch was removed. Bug in the is.na code???
	mutate(intolerant=ifelse(is.na(intolerant),"nopli",intolerant)) %>% #change NA to a label on the plot I can control
	mutate(intolerant=factor(intolerant, levels=c("nopli","Tolerant","Intolerant"))) #This sets the order of the levels on the plots below


cistrans_categories <- data.frame(cis="cis", trans_inter="trans\nInterchromosomal", trans_intra="trans\nIntrachromosomal", noeQTL="No eQTL")
cistrans_colours <- c(cis=brewer.pal(8,"Dark2")[1], trans_inter=brewer.pal(8,"Dark2")[3], trans_intra=brewer.pal(8,"Dark2")[2], noeQTL="black")

#both phenotypes in one facet plot
p_pheno_pLI <- ggplot(table_in_pheno, aes(x=factor(cistrans), y=pLI, fill=factor(cistrans), color=factor(cistrans))) +
	#facet_wrap(~cohesin_gene_list) +
	geom_eye(scale="width", position = position_dodge(width = .3)) +
	#geom_quasirandom(alpha = 0.3, width = 0.5, size = 1.5, dodge.width=.8) +

	scale_color_manual(values=cistrans_colours, guide=FALSE) + #color of x-axis sep
	scale_fill_manual(values=lapply(cistrans_colours,alpha, 0.5), labels=cistrans_categories) + #color of x-axis sep violin
	stat_summary(aes(label=round(..y..,2)), fun.y=median, geom="text", size=14, hjust=-0.1, vjust = 0.5, show.legend=FALSE, position = position_dodge(width = .55)) + 
	
	#add horizontal lines for pLI 0.9
	geom_hline(aes(yintercept= as.numeric(0.9)), colour = "red", size = 2) +
	annotate(geom="text", label="pLI=0.9", x=0, y=0.9, hjust=-0.2, vjust=-0.7, size=12) +
	
	scale_x_discrete(labels=cistrans_categories) + 
	scale_y_continuous(limits=c(0,1)) + 

    # Add highlighted points
    #geom_point(data=subset(don_notGBA_trans_intra, is_highlight=="yes"), color="green", size=2) +
  
    # Add label using ggrepel to avoid overlapping
    #geom_label_repel(data=subset(table_in_cohesin, cohesin_gene_list=="TRUE"), aes(label=gene), size=6) +

    # Custom theme:
	theme_bw() + 
	#theme(legend.position="none") + 
    theme( 
		panel.border = element_rect(fill=NA, size=3),
		axis.text=element_text(size=36, family="ArialMT"),
		axis.title=element_text(size=42, family="ArialMT"),
		axis.line = element_line(colour = 'black', size = 2),
		plot.title = element_text(size=54, margin = margin(t = 0, r = 0, b = 30, l = 0), hjust = 0.5, family="ArialMT"),
		legend.title = element_text(colour="black", size = 36),
		legend.text = element_text(colour="black", size = 24)
	) + 
	labs(x = "eQTL Distance", y="Probability of Loss-of-Function-Intolerance", title = "gnomAD Loss-of-Function (LoF)-Intolerance", fill="eQTL Distance")
ggsave("/Volumes/resmed201800011-foffa/Archive/projects/P1_ND_and_Cogntiion/pLI/ASD_pLI_cistrans.pdf", plot = p_pheno_pLI, width=40, height=20)

intolerant_colours <- c(Intolerant=brewer.pal(9,"Blues")[4], Tolerant=brewer.pal(9,"Blues")[8], nopli="black")
intolerant_categories <- data.frame(Intolerant="Intolerant", Tolerant="Tolerant", nopli="Missing pLI")

p_pheno_pLI_bar <- ggplot(table_in_pheno2, aes(x=factor(cistrans), fill=factor(intolerant))) +
	geom_bar(position = "fill") +
	scale_x_discrete(labels=cistrans_categories) + 
	scale_y_continuous(labels = scales::percent) +

	scale_fill_manual(values=intolerant_colours, labels=intolerant_categories) + #color of x-axis sep violin
	
    # Custom theme:
	theme_bw() + 
    theme( 
		panel.border = element_rect(fill=NA, size=3),
		axis.text=element_text(size=36, family="ArialMT"),
		axis.title=element_text(size=42, family="ArialMT"),
		axis.line = element_line(colour = 'black', size = 2),
		plot.title = element_text(size=54, margin = margin(t = 0, r = 0, b = 30, l = 0), hjust = 0.5, family="ArialMT"),
		legend.title = element_text(colour="black", size = 36),
		legend.text = element_text(colour="black", size = 24)
	) + 
	labs(x = "eQTL Distance", y="Proportion of Samples", title = "gnomAD Loss-of-Function (LoF)-Intolerance", fill="gnomAD LoF\n(pLI > 0.9)")
ggsave("/Volumes/resmed201800011-foffa/Archive/projects/P1_ND_and_Cogntiion/pLI/ASD_pLI_cistrans_intolerance_proportional_bars.pdf", plot = p_pheno_pLI_bar, width=40, height=20)
