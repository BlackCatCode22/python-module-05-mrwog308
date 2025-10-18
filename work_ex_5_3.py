#Regular expressions exercise 5_3
import re

mtext = open('mbox-short.txt')
dlist = []
for mline in mtext:
    mline = mline.rstrip()
    mstuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', mline)
    if len(mstuff) != 1 : continue
    mnum = float(mstuff[0])
    dlist.append(mnum)
print('Maximum:', max(dlist))
