import numpy as np
import pandas as pd
from optparse import OptionParser

parser = OptionParser()

parser.add_option('--dbName', type='str', default='flexddf_v1.4_10yrs_DD',
                  help='db name [%default]')
parser.add_option('--config', type='str', default='scen1',
                  help='configuration - should correspond to a config.csv file [%default]')
parser.add_option('--dirConfig', type='str',
                  default='input/reshuffling',
                  help="config files location [%default]")


opts, args = parser.parse_args()
dbName = opts.dbName
config = opts.config
dirConfig = opts.dirConfig

# load datas
tab = pd.DataFrame(
    np.load('{}_with_fields.npy'.format(dbName), allow_pickle=True))

# get the number of visits to be implemented
nvisits = pd.read_csv('{}/{}.csv'.format(dirConfig, config)
                      ).to_dict(orient='records')[0]

# correct for the number of exposures and times
tab['numExposures'] = tab.apply(lambda x: nvisits[x['band']], axis=1)
tab['exptime'] *= tab['numExposures']
tab['visitTime'] *= tab['numExposures']

# remove dithering (if any)
#tab['fieldRA'] = tab.groupby(['fieldName'])['fieldRA'].transform('mean')
#tab['fieldDec'] = tab.groupby(['fieldName'])['fieldDec'].transform('mean')


# get medians
med_night = tab.groupby(['fieldName', 'night',
                         'band', 'season']).median().reset_index()

# m5 should also be modified
med_night['fiveSigmaDepth'] += 1.25*np.log(med_night['numExposures'])

# remove columns associated to DD fields
"""
todrop = ['fieldName', 'healpixID', 'pixRA',
          'pixDec', 'ebv', 'RA', 'Dec', 'season']
"""
#todrop = ['RA', 'Dec', 'season']
#finaldf = med_night.drop(columns=todrop)

finaldf = med_night
print(finaldf.columns)

print(finaldf[['exptime', 'numExposures',
               'visitTime', 'fiveSigmaDepth', 'RA', 'Dec']])

# save in npy file

np.save('{}_{}.npy'.format(dbName, config), finaldf.to_records(index=False))
