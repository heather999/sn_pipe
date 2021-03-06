import glob
import numpy as np
from optparse import OptionParser

def genFile(files,fName,postfix):
    """
    Method to generate a file of OS names and associated infos
    This file is used as an input file to metrics, simulations in batch


    Parameters
    ---------
    files: list(str)
     list of files
    fName: str
      fName of the output file
    postfix: str
      infos associated to the OS
    
    """

    script = open(fName,"w")
    #firstline='# dbName			simuType	  nside  coadd fieldtype nproc\n'
    firstline='dbName,simuType,nside,coadd,fieldtype,nproc\n'
    script.write(firstline)
    r = []
    for fi in files:
        dbName = fi.split('/')[-1].split('.db')[0]
        r.append(len(dbName))
        #ljust = np.max(r)

    for fi in files:
        dbName = fi.split('/')[-1].split('.db')[0]
        #dbName=dbName.ljust(ljust)
        line='{},{}\n'.format(dbName,postfix)
        print(line)
        script.write(line)

    script.close()


parser = OptionParser()

parser.add_option("--simuVersion", type=str, default='fbs_14',
                  help="simulation version[%default]")

parser.add_option("--dirFiles", type=str, default='/sps/lsst/cadence/LSST_SN_PhG/cadence_db/fbs_1.4/db',
                  help="dir where the files are [%default]")

opts, args = parser.parse_args()

simuVersion = opts.simuVersion
dirFiles = opts.dirFiles

files = glob.glob('{}/*.db'.format(dirFiles))

print(files)

#DD_postfix = '1	     128    1	  DD	    6'
#WFD_postfix = '0	     64    1	  WFD	    8'

DD_postfix = '1,128,1,DD,6'
WFD_postfix = '0,64,1,WFD,8'

print(DD_postfix)
genFile(files,'DD_{}.csv'.format(simuVersion),DD_postfix)
genFile(files,'WFD_{}.csv'.format(simuVersion),WFD_postfix)
