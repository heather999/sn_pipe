import glob
import numpy as np

def genFile(files,fName,postfix):

    script = open(fName,"w")
    firstline='# dbName			simuType	  nside  coadd fieldtype nproc\n'
    script.write(firstline)
    r = []
    for fi in files:
    	dbName = fi.split('/')[-1].split('.db')[0]
    	r.append(len(dbName))

    ljust = np.max(r)
    for fi in files:
    	dbName = fi.split('/')[-1].split('.db')[0]
    	dbName=dbName.ljust(ljust)
    	line = '{} {}\n'.format(dbName,postfix)
    	print(line)
    	script.write(line)

    script.close()

fbsvers = 'fbs_1.5'
dirFiles = '/sps/lsst/cadence/LSST_SN_PhG/cadence_db/{}/db'.format(fbsvers)

files = glob.glob('{}/*.db'.format(dirFiles))

print(files)

DD_postfix = '1	     128    1	  DD	    6'
WFD_postfix = '0	     64    1	  WFD	    8'

genFile(files,'DD_fbs15.txt',DD_postfix)
genFile(files,'WFD_fbs15.txt',WFD_postfix)