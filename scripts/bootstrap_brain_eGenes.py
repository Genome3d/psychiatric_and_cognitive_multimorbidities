from __future__ import division
import random
import numpy as np
import csv



tests = input("Enter number of tests to be done and press enter \n") # Use 10000

print("\n Bootstrapping in process......., Please Wait !!!!!! \n")

temp = []


allgene = list(line.strip() for line in open("all_genes.txt"))
f = open('statistics.txt', 'w')
writer = csv.writer(f, delimiter='\t')

header = ['adhd_anx_bd_ud_scz_cog', 'adhd_anx_bd_ud_scz', 'adhd_anx_scz_ud_cog', 'adhd_bd_scz_ud_cog', 'anx_bd_scz_ud_cog', 'adhd_anx_bd_ud_cog', 'adhd_anx_bd_scz_cog',
'adhd_bd_scz_ud', 'anx_bd_ud_cog', 'anx_scz_ud_cog', 'bd_scz_ud_cog', 'anx_bd_scz_cog', 'anx_bd_scz_ud', 'adhd_scz_ud_cog', 'adhd_bd_ud_cog', 'adhd_bd_scz_cog', 'adhd_anx_ud_cog', 'adhd_anx_scz_cog', 'adhd_anx_scz_ud', 'adhd_anx_bd_cog', 'adhd_anx_bd_ud', 'adhd_anx_bd_scz', 
'anx_bd_scz', 'adhd_scz_ud', 'anx_scz_ud', 'bd_scz_ud', 'bd_scz_cog', 'anx_ud_cog', 'scz_ud_cog', 'bd_ud_cog', 'anx_scz_cog', 'anx_bd_cog', 'anx_bd_ud', 'adhd_ud_cog', 'adhd_scz_cog', 'adhd_bd_cog', 'adhd_bd_ud', 'adhd_bd_scz', 'adhd_anx_cog', 'adhd_anx_ud', 'adhd_anx_scz', 'adhd_anx_bd', 
'adhd_anx', 'bd_scz', 'anx_ud', 'bd_ud', 'scz_ud', 'anx_cog', 'bd_cog', 'ud_cog', 'scz_cog', 'anx_scz', 'anx_bd', 'adhd_cog', 'adhd_ud', 'adhd_scz', 'adhd_bd']

writer.writerow(header)
for i in range(0, tests):
# Rangom lists of genes:

    adhd = set(np.random.choice(allgene, 51, replace= True))
    anx = set(np.random.choice(allgene, 134, replace= True))
    bd = set(np.random.choice(allgene, 89, replace= True))
    ud = set(np.random.choice(allgene, 278, replace= True))
    sch = set(np.random.choice(allgene, 266, replace= True))
    cog = set(np.random.choice(allgene, 255, replace= True))


    adhd_anx_bd_ud_sch_cog = list(adhd & anx & bd & ud & sch & cog)
    adhd_anx_bd_ud_sch = list(adhd & anx & bd & ud & sch)
    adhd_anx_sch_ud_cog = list(adhd & anx & sch & ud & cog)
    adhd_bd_sch_ud_cog = list(adhd & bd & sch & ud & cog)
    anx_bd_sch_ud_cog = list(anx & bd & sch & ud & cog)
    adhd_anx_bd_ud_cog = list(adhd & anx & bd & ud & cog)
    adhd_anx_bd_sch_cog = list(adhd & anx & bd & sch & cog)
    adhd_bd_sch_ud = list(adhd & bd & sch & ud)
    anx_bd_ud_cog = list(anx & bd & cog & ud)
    anx_sch_ud_cog = list(anx & sch & ud & cog)
    bd_sch_ud_cog = list(bd & sch & ud & cog)
    anx_bd_sch_cog = list(anx & bd & sch & cog)
    anx_bd_sch_ud = list(anx & bd & sch & ud)
    adhd_sch_ud_cog = list(adhd & sch & ud & cog)
    adhd_bd_ud_cog = list(adhd & bd & ud & cog)
    adhd_bd_sch_cog = list(adhd & bd & sch & cog)
    adhd_anx_ud_cog = list(adhd & anx & ud & cog)
    adhd_anx_sch_cog = list(adhd & anx & sch & cog)
    adhd_anx_sch_ud = list(adhd & anx & sch & ud)
    adhd_anx_bd_cog = list(adhd & anx & bd & cog)
    adhd_anx_bd_ud = list(adhd & anx & bd & ud)
    adhd_anx_bd_sch = list(adhd & anx & bd & sch)
    anx_bd_sch = list(anx & bd & sch)
    adhd_sch_ud = list(adhd & sch & ud)
    anx_sch_ud = list(anx & sch & ud)
    bd_sch_ud = list(bd & sch & ud)
    bd_sch_cog = list(bd & sch & cog)
    anx_ud_cog = list(anx & ud & cog)
    sch_ud_cog = list(sch & ud & cog)
    bd_ud_cog = list(bd & ud & cog)
    anx_sch_cog = list(anx & sch & cog)
    anx_bd_cog = list(anx & bd & cog)
    anx_bd_ud = list(anx & bd & ud)
    adhd_ud_cog = list(adhd & ud & cog)
    adhd_sch_cog = list(adhd & sch & cog)
    adhd_bd_cog = list(adhd & bd & cog)
    adhd_bd_ud = list(adhd & bd & ud)
    adhd_bd_sch = list(adhd & bd & sch)
    adhd_anx_cog = list(adhd & anx & cog)
    adhd_anx_ud = list(adhd & anx & ud)
    adhd_anx_sch = list(adhd & anx & sch)
    adhd_anx_bd = list(adhd & anx & bd)
    adhd_anx = list(adhd & anx)
    bd_sch = list(bd & sch)
    anx_ud = list(anx & ud)
    bd_ud = list(bd & ud)
    sch_ud = list(sch & ud)
    anx_cog = list(anx & cog)
    bd_cog = list(bd & cog)
    ud_cog = list(ud & cog)
    sch_cog = list(sch & cog)
    anx_sch = list(anx & sch)
    anx_bd = list(anx & bd)
    adhd_cog = list(adhd & cog)
    adhd_ud = list(adhd & ud)
    adhd_sch = list(adhd & sch)
    adhd_bd = list(adhd & bd)


    len_adhd_anx_bd_ud_sch_cog = len(adhd_anx_bd_ud_sch_cog)
    len_adhd_anx_bd_ud_sch = len(adhd_anx_bd_ud_sch)
    len_adhd_anx_sch_ud_cog = len(adhd_anx_sch_ud_cog)
    len_adhd_bd_sch_ud_cog = len(adhd_bd_sch_ud_cog)
    len_anx_bd_sch_ud_cog = len(anx_bd_sch_ud_cog)
    len_adhd_anx_bd_ud_cog = len(adhd_anx_bd_ud_cog)
    len_adhd_anx_bd_sch_cog = len(adhd_anx_bd_sch_cog)
    len_adhd_bd_sch_ud = len(adhd_bd_sch_ud)
    len_anx_bd_ud_cog = len(anx_bd_ud_cog)
    len_anx_sch_ud_cog = len(anx_sch_ud_cog)
    len_bd_sch_ud_cog = len(bd_sch_ud_cog)
    len_anx_bd_sch_cog = len(anx_bd_sch_cog)
    len_anx_bd_sch_ud = len(anx_bd_sch_ud)
    len_adhd_sch_ud_cog = len(adhd_sch_ud_cog)
    len_adhd_bd_ud_cog = len(adhd_bd_ud_cog)
    len_adhd_bd_sch_cog = len(adhd_bd_sch_cog)
    len_adhd_anx_ud_cog = len(adhd_anx_ud_cog)
    len_adhd_anx_sch_cog = len(adhd_anx_sch_cog)
    len_adhd_anx_sch_ud = len(adhd_anx_sch_ud)
    len_adhd_anx_bd_cog = len(adhd_anx_bd_cog)
    len_adhd_anx_bd_ud = len(adhd_anx_bd_ud)
    len_adhd_anx_bd_sch = len(adhd_anx_bd_sch)
    len_anx_bd_sch = len(anx_bd_sch)
    len_adhd_sch_ud = len(adhd_sch_ud)
    len_anx_sch_ud = len(anx_sch_ud)
    len_bd_sch_ud = len(bd_sch_ud)
    len_bd_sch_cog = len(bd_sch_cog)
    len_anx_ud_cog = len(anx_ud_cog)
    len_sch_ud_cog = len(sch_ud_cog)
    len_bd_ud_cog = len(bd_ud_cog)
    len_anx_sch_cog = len(anx_sch_cog)
    len_anx_bd_cog = len(anx_bd_cog)
    len_anx_bd_ud = len(anx_bd_ud)
    len_adhd_ud_cog = len(adhd_ud_cog)
    len_adhd_sch_cog = len(adhd_sch_cog)
    len_adhd_bd_cog = len(adhd_bd_cog)
    len_adhd_bd_ud = len(adhd_bd_ud)
    len_adhd_bd_sch = len(adhd_bd_sch)
    len_adhd_anx_cog = len(adhd_anx_cog)
    len_adhd_anx_ud = len(adhd_anx_ud)
    len_adhd_anx_sch = len(adhd_anx_sch)
    len_adhd_anx_bd = len(adhd_anx_bd)
    len_adhd_anx = len(adhd_anx)
    len_bd_sch = len(bd_sch)
    len_anx_ud = len(anx_ud)
    len_bd_ud = len(bd_ud)
    len_sch_ud = len(sch_ud)
    len_anx_cog = len(anx_cog)
    len_bd_cog = len(bd_cog)
    len_ud_cog = len(ud_cog)
    len_sch_cog = len(sch_cog)
    len_anx_sch = len(anx_sch)
    len_anx_bd = len(anx_bd)
    len_adhd_cog = len(adhd_cog)
    len_adhd_ud = len(adhd_ud)
    len_adhd_sch = len(adhd_sch)
    len_adhd_bd = len(adhd_bd)


    combined = [len_adhd_anx_bd_ud_sch_cog, 
    len_adhd_anx_bd_ud_sch, len_adhd_anx_sch_ud_cog, len_adhd_bd_sch_ud_cog, len_anx_bd_sch_ud_cog, len_adhd_anx_bd_ud_cog, len_adhd_anx_bd_sch_cog,
    len_adhd_bd_sch_ud, len_anx_bd_ud_cog, len_anx_sch_ud_cog, len_bd_sch_ud_cog, len_anx_bd_sch_cog, len_anx_bd_sch_ud, len_adhd_sch_ud_cog, len_adhd_bd_ud_cog, len_adhd_bd_sch_cog, len_adhd_anx_ud_cog, len_adhd_anx_sch_cog, len_adhd_anx_sch_ud, len_adhd_anx_bd_cog, len_adhd_anx_bd_ud, len_adhd_anx_bd_sch, 
    len_anx_bd_sch, len_adhd_sch_ud, len_anx_sch_ud, len_bd_sch_ud, len_bd_sch_cog, len_anx_ud_cog, len_sch_ud_cog, len_bd_ud_cog, len_anx_sch_cog, len_anx_bd_cog, len_anx_bd_ud, len_adhd_ud_cog, len_adhd_sch_cog, len_adhd_bd_cog, len_adhd_bd_ud, len_adhd_bd_sch, len_adhd_anx_cog, len_adhd_anx_ud, len_adhd_anx_sch, len_adhd_anx_bd, 
    len_adhd_anx, len_bd_sch, len_anx_ud, len_bd_ud, len_sch_ud, len_anx_cog, len_bd_cog, len_ud_cog, len_sch_cog, len_anx_sch, len_anx_bd, len_adhd_cog, len_adhd_ud, len_adhd_sch, len_adhd_bd]

    writer.writerows([combined])

    if  (len_adhd_anx_bd_ud_sch_cog >= 6):
        temp.append(1)
    else:
        pass
    if (len_adhd_anx_bd_ud_sch >= 13):
        temp.append(2)
    else:
        pass
    if (len_adhd_anx_sch_ud_cog >= 6):
        temp.append(3)
    else:
        pass
    if (len_adhd_bd_sch_ud_cog >= 9):
        temp.append(4)
    else:
        pass
    if (len_anx_bd_sch_ud_cog >= 8):
        temp.append(5)
    else:
        pass
    if (len_adhd_anx_bd_ud_cog >= 6):
        temp.append(6)
    else:
        pass
    if (len_adhd_anx_bd_sch_cog >= 6):
        temp.append(7)
    else:
        pass
    if (len_adhd_bd_sch_ud >= 32):
        temp.append(8)
    else:
        pass
    if (len_anx_bd_ud_cog >= 8):
        temp.append(9)
    else:
        pass
    if (len_anx_sch_ud_cog >= 9):
        temp.append(10)
    else:
        pass
    if (len_bd_sch_ud_cog >= 12):
        temp.append(11)
    else:
        pass
    if (len_anx_bd_sch_cog >= 9):
        temp.append(12)
    else:
        pass
    if (len_anx_bd_sch_ud >= 15):
        temp.append(13)
    else:
        pass
    if (len_adhd_sch_ud_cog >= 9):
        temp.append(14)
    else:
        pass
    if (len_adhd_bd_ud_cog >= 9):
        temp.append(15)
    else:
        pass
    if (len_adhd_bd_sch_cog >= 9):
        temp.append(16)
    else:
        pass
    if (len_adhd_anx_ud_cog >= 6):
        temp.append(17)
    else:
        pass
    if (len_adhd_anx_sch_cog >= 6):
        temp.append(18)
    else:
        pass
    if (len_adhd_anx_sch_ud >= 13):
        temp.append(19)
    else:
        pass
    if (len_adhd_anx_bd_cog >= 6):
        temp.append(20)
    else:
        pass
    if (len_adhd_anx_bd_ud >= 13):
        temp.append(21)
    else:
        pass
    if (len_adhd_anx_bd_sch >= 13):
        temp.append(22)
    else:
        pass
    if (len_anx_bd_sch >= 16):
        temp.append(23)
    else:
        pass
    if (len_adhd_sch_ud >= 33):
        temp.append(24)
    else:
        pass
    if (len_anx_sch_ud >= 16):
        temp.append(25)
    else:
        pass
    if (len_bd_sch_ud >= 39):
        temp.append(26)
    else:
        pass
    if (len_bd_sch_cog >= 15):
        temp.append(27)
    else:
        pass
    if (len_anx_ud_cog >= 25):
        temp.append(28)
    else:
        pass
    if (len_sch_ud_cog >= 18):
        temp.append(29)
    else:
        pass
    if (len_bd_ud_cog >= 12):
        temp.append(30)
    else:
        pass
    if (len_anx_sch_cog >= 13):
        temp.append(31)
    else:
        pass
    if (len_anx_bd_cog >= 9):
        temp.append(32)
    else:
        pass
    if (len_anx_bd_ud >= 15):
        temp.append(33)
    else:
        pass
    if (len_adhd_ud_cog >= 9):
        temp.append(34)
    else:
        pass
    if (len_adhd_sch_cog >= 9):
        temp.append(35)
    else:
        pass
    if (len_adhd_bd_cog >= 9):
        temp.append(36)
    else:
        pass
    if (len_adhd_bd_ud >= 35):
        temp.append(37)
    else:
        pass
    if (len_adhd_bd_sch >= 32):
        temp.append(38)
    else:
        pass
    if (len_adhd_anx_cog >= 6):
        temp.append(39)
    else:
        pass
    if (len_adhd_anx_ud >= 13):
        temp.append(40)
    else:
        pass
    if (len_adhd_anx_sch >= 13):
        temp.append(41)
    else:
        pass
    if (len_adhd_anx_bd >= 13):
        temp.append(42)
    else:
        pass
    if (len_adhd_anx >= 14):
        temp.append(43)
    else:
        pass
    if (len_bd_sch >= 57):
        temp.append(44)
    else:
        pass
    if (len_anx_ud >= 39):
        temp.append(45)
    else:
        pass
    if (len_bd_ud >= 44):
        temp.append(46)
    else:
        pass
    if (len_sch_ud >= 75):
        temp.append(47)
    else:
        pass
    if (len_anx_cog >= 39):
        temp.append(48)
    else:
        pass
    if (len_bd_cog >= 19):
        temp.append(49)
    else:
        pass
    if (len_ud_cog >= 58):
        temp.append(50)
    else:
        pass
    if (len_sch_cog >= 37):
        temp.append(51)
    else:
        pass
    if (len_anx_sch >= 25):
        temp.append(52)
    else:
        pass
    if (len_anx_bd >= 16):
        temp.append(53)
    else:
        pass
    if (len_adhd_cog >= 9):
        temp.append(54)
    else:
        pass
    if (len_adhd_ud >= 37):
        temp.append(55)
    else:
        pass
    if (len_adhd_sch >= 34):
        temp.append(56)
    else:
        pass
    if (len_adhd_bd >= 37):
        temp.append(57)
    else:
        pass


adhd_anx_bd_ud_sch_cog_temp = temp.count(1)
adhd_anx_bd_ud_sch_temp = temp.count(2)
adhd_anx_sch_ud_cog_temp = temp.count(3)
adhd_bd_sch_ud_cog_temp = temp.count(4)
anx_bd_sch_ud_cog_temp = temp.count(5)
adhd_anx_bd_ud_cog_temp = temp.count(6)
adhd_anx_bd_sch_cog_temp = temp.count(7)
adhd_bd_sch_ud_temp = temp.count(8)
anx_bd_ud_cog_temp = temp.count(9)
anx_sch_ud_cog_temp = temp.count(10)
bd_sch_ud_cog_temp = temp.count(11)
anx_bd_sch_cog_temp = temp.count(12)
anx_bd_sch_ud_temp = temp.count(13)
adhd_sch_ud_cog_temp = temp.count(14)
adhd_bd_ud_cog_temp = temp.count(15)
adhd_bd_sch_cog_temp = temp.count(16)
adhd_anx_ud_cog_temp = temp.count(17)
adhd_anx_sch_cog_temp = temp.count(18)
adhd_anx_sch_ud_temp = temp.count(19)
adhd_anx_bd_cog_temp = temp.count(20)
adhd_anx_bd_ud_temp = temp.count(21)
adhd_anx_bd_sch_temp = temp.count(22)
anx_bd_sch_temp = temp.count(23)
adhd_sch_ud_temp = temp.count(24)
anx_sch_ud_temp = temp.count(25)
bd_sch_ud_temp = temp.count(26)
bd_sch_cog_temp = temp.count(27)
anx_ud_cog_temp = temp.count(28)
sch_ud_cog_temp = temp.count(29)
bd_ud_cog_temp = temp.count(30)
anx_sch_cog_temp = temp.count(31)
anx_bd_cog_temp = temp.count(32)
anx_bd_ud_temp = temp.count(33)
adhd_ud_cog_temp = temp.count(34)
adhd_sch_cog_temp = temp.count(35)
adhd_bd_cog_temp = temp.count(36)
adhd_bd_ud_temp = temp.count(37)
adhd_bd_sch_temp = temp.count(38)
adhd_anx_cog_temp = temp.count(39)
adhd_anx_ud_temp = temp.count(40)
adhd_anx_sch_temp = temp.count(41)
adhd_anx_bd_temp = temp.count(42)
adhd_anx_temp = temp.count(43)
bd_sch_temp = temp.count(44)
anx_ud_temp = temp.count(45)
bd_ud_temp = temp.count(46)
sch_ud_temp = temp.count(47)
anx_cog_temp = temp.count(48)
bd_cog_temp = temp.count(49)
ud_cog_temp = temp.count(50)
sch_cog_temp = temp.count(51)
anx_sch_temp = temp.count(52)
anx_bd_temp = temp.count(53)
adhd_cog_temp = temp.count(54)
adhd_ud_temp = temp.count(55)
adhd_sch_temp = temp.count(56)
adhd_bd_temp = temp.count(57)


pval_adhd_anx_bd_ud_sch_cog_temp = adhd_anx_bd_ud_sch_cog_temp/tests
pval_adhd_anx_bd_ud_sch_temp = adhd_anx_bd_ud_sch_temp/tests
pval_adhd_anx_sch_ud_cog_temp = adhd_anx_sch_ud_cog_temp/tests
pval_adhd_bd_sch_ud_cog_temp = adhd_bd_sch_ud_cog_temp/tests
pval_anx_bd_sch_ud_cog_temp = anx_bd_sch_ud_cog_temp/tests
pval_adhd_anx_bd_ud_cog_temp = adhd_anx_bd_ud_cog_temp/tests
pval_adhd_anx_bd_sch_cog_temp = adhd_anx_bd_sch_cog_temp/tests
pval_adhd_bd_sch_ud_temp = adhd_bd_sch_ud_temp/tests
pval_anx_bd_ud_cog_temp = anx_bd_ud_cog_temp/tests
pval_anx_sch_ud_cog_temp = anx_sch_ud_cog_temp/tests
pval_bd_sch_ud_cog_temp = bd_sch_ud_cog_temp/tests
pval_anx_bd_sch_cog_temp = anx_bd_sch_cog_temp/tests
pval_anx_bd_sch_ud_temp = anx_bd_sch_ud_temp/tests
pval_adhd_sch_ud_cog_temp = adhd_sch_ud_cog_temp/tests
pval_adhd_bd_ud_cog_temp = adhd_bd_ud_cog_temp/tests
pval_adhd_bd_sch_cog_temp = adhd_bd_sch_cog_temp/tests
pval_adhd_anx_ud_cog_temp = adhd_anx_ud_cog_temp/tests
pval_adhd_anx_sch_cog_temp = adhd_anx_sch_cog_temp/tests
pval_adhd_anx_sch_ud_temp = adhd_anx_sch_ud_temp/tests
pval_adhd_anx_bd_cog_temp = adhd_anx_bd_cog_temp/tests
pval_adhd_anx_bd_ud_temp = adhd_anx_bd_ud_temp/tests
pval_adhd_anx_bd_sch_temp = adhd_anx_bd_sch_temp/tests
pval_anx_bd_sch_temp = anx_bd_sch_temp/tests
pval_adhd_sch_ud_temp = adhd_sch_ud_temp/tests
pval_anx_sch_ud_temp = anx_sch_ud_temp/tests
pval_bd_sch_ud_temp = bd_sch_ud_temp/tests
pval_bd_sch_cog_temp = bd_sch_cog_temp/tests
pval_anx_ud_cog_temp = anx_ud_cog_temp/tests
pval_sch_ud_cog_temp = sch_ud_cog_temp/tests
pval_bd_ud_cog_temp = bd_ud_cog_temp/tests
pval_anx_sch_cog_temp = anx_sch_cog_temp/tests
pval_anx_bd_cog_temp = anx_bd_cog_temp/tests
pval_anx_bd_ud_temp = anx_bd_ud_temp/tests
pval_adhd_ud_cog_temp = adhd_ud_cog_temp/tests
pval_adhd_sch_cog_temp = adhd_sch_cog_temp/tests
pval_adhd_bd_cog_temp = adhd_bd_cog_temp/tests
pval_adhd_bd_ud_temp = adhd_bd_ud_temp/tests
pval_adhd_bd_sch_temp = adhd_bd_sch_temp/tests
pval_adhd_anx_cog_temp = adhd_anx_cog_temp/tests
pval_adhd_anx_ud_temp = adhd_anx_ud_temp/tests
pval_adhd_anx_sch_temp = adhd_anx_sch_temp/tests
pval_adhd_anx_bd_temp = adhd_anx_bd_temp/tests
pval_adhd_anx_temp = adhd_anx_temp/tests
pval_bd_sch_temp = bd_sch_temp/tests
pval_anx_ud_temp = anx_ud_temp/tests
pval_bd_ud_temp = bd_ud_temp/tests
pval_sch_ud_temp = sch_ud_temp/tests
pval_anx_cog_temp = anx_cog_temp/tests
pval_bd_cog_temp = bd_cog_temp/tests
pval_ud_cog_temp = ud_cog_temp/tests
pval_sch_cog_temp = sch_cog_temp/tests
pval_anx_sch_temp = anx_sch_temp/tests
pval_anx_bd_temp = anx_bd_temp/tests
pval_adhd_cog_temp = adhd_cog_temp/tests
pval_adhd_ud_temp = adhd_ud_temp/tests
pval_adhd_sch_temp = adhd_sch_temp/tests
pval_adhd_bd_temp = adhd_bd_temp/tests


f1 = open('pvalues.txt', 'w')
writer = csv.writer(f1, delimiter = '\t')

header = ['pval_adhd_anx_bd_ud_scz_cog_temp', 
'pval_adhd_anx_bd_ud_scz_temp', 'pval_adhd_anx_scz_ud_cog_temp', 'pval_adhd_bd_scz_ud_cog_temp', 'pval_anx_bd_scz_ud_cog_temp', 'pval_adhd_anx_bd_ud_cog_temp', 'pval_adhd_anx_bd_scz_cog_temp',
'pval_adhd_bd_scz_ud_temp', 'pval_anx_bd_ud_cog_temp', 'pval_anx_scz_ud_cog_temp', 'pval_bd_scz_ud_cog_temp', 'pval_anx_bd_scz_cog_temp', 'pval_anx_bd_scz_ud_temp', 'pval_adhd_scz_ud_cog_temp', 'pval_adhd_bd_ud_cog_temp', 'pval_adhd_bd_scz_cog_temp', 'pval_adhd_anx_ud_cog_temp', 'pval_adhd_anx_scz_cog_temp', 'pval_adhd_anx_scz_ud_temp', 'pval_adhd_anx_bd_cog_temp', 'pval_adhd_anx_bd_ud_temp', 'pval_adhd_anx_bd_scz_temp', 
'pval_anx_bd_scz_temp', 'pval_adhd_scz_ud_temp', 'pval_anx_scz_ud_temp', 'pval_bd_scz_ud_temp', 'pval_bd_scz_cog_temp', 'pval_anx_ud_cog_temp', 'pval_scz_ud_cog_temp', 'pval_bd_ud_cog_temp', 'pval_anx_scz_cog_temp', 'pval_anx_bd_cog_temp', 'pval_anx_bd_ud_temp', 'pval_adhd_ud_cog_temp', 'pval_adhd_scz_cog_temp', 'pval_adhd_bd_cog_temp', 'pval_adhd_bd_ud_temp', 'pval_adhd_bd_scz_temp', 'pval_adhd_anx_cog_temp', 'pval_adhd_anx_ud_temp', 'pval_adhd_anx_scz_temp', 'pval_adhd_anx_bd_temp', 
'pval_adhd_anx_temp', 'pval_bd_scz_temp', 'pval_anx_ud_temp', 'pval_bd_ud_temp', 'pval_scz_ud_temp', 'pval_anx_cog_temp', 'pval_bd_cog_temp', 'pval_ud_cog_temp', 'pval_scz_cog_temp', 'pval_anx_scz_temp', 'pval_anx_bd_temp', 'pval_adhd_cog_temp', 'pval_adhd_ud_temp', 'pval_adhd_scz_temp', 'pval_adhd_bd_temp']

writer.writerow(header)

pvalue = [pval_adhd_anx_bd_ud_sch_cog_temp, 
pval_adhd_anx_bd_ud_sch_temp, pval_adhd_anx_sch_ud_cog_temp, pval_adhd_bd_sch_ud_cog_temp, pval_anx_bd_sch_ud_cog_temp, pval_adhd_anx_bd_ud_cog_temp, pval_adhd_anx_bd_sch_cog_temp,
pval_adhd_bd_sch_ud_temp, pval_anx_bd_ud_cog_temp, pval_anx_sch_ud_cog_temp, pval_bd_sch_ud_cog_temp, pval_anx_bd_sch_cog_temp, pval_anx_bd_sch_ud_temp, pval_adhd_sch_ud_cog_temp, pval_adhd_bd_ud_cog_temp, pval_adhd_bd_sch_cog_temp, pval_adhd_anx_ud_cog_temp, pval_adhd_anx_sch_cog_temp, pval_adhd_anx_sch_ud_temp, pval_adhd_anx_bd_cog_temp, pval_adhd_anx_bd_ud_temp, pval_adhd_anx_bd_sch_temp, 
pval_anx_bd_sch_temp, pval_adhd_sch_ud_temp, pval_anx_sch_ud_temp, pval_bd_sch_ud_temp, pval_bd_sch_cog_temp, pval_anx_ud_cog_temp, pval_sch_ud_cog_temp, pval_bd_ud_cog_temp, pval_anx_sch_cog_temp, pval_anx_bd_cog_temp, pval_anx_bd_ud_temp, pval_adhd_ud_cog_temp, pval_adhd_sch_cog_temp, pval_adhd_bd_cog_temp, pval_adhd_bd_ud_temp, pval_adhd_bd_sch_temp, pval_adhd_anx_cog_temp, pval_adhd_anx_ud_temp, pval_adhd_anx_sch_temp, pval_adhd_anx_bd_temp, 
pval_adhd_anx_temp, pval_bd_sch_temp, pval_anx_ud_temp, pval_bd_ud_temp, pval_sch_ud_temp, pval_anx_cog_temp, pval_bd_cog_temp, pval_ud_cog_temp, pval_sch_cog_temp, pval_anx_sch_temp, pval_anx_bd_temp, pval_adhd_cog_temp, pval_adhd_ud_temp, pval_adhd_sch_temp, pval_adhd_bd_temp]

writer.writerows([pvalue])

f.close()
f1.close()

print("Bootrapping Done!!! \n")
print("Two output files statistics.txt and pvalues.txt are generated. \n")
print("Have FUN!!! \n")
