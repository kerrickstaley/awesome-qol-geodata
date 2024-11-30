# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import polars as pl
import requests

# %%
# Choose any email for AQS_EMAIL, then visit https://aqs.epa.gov/data/api/signup?email=<your email> to get the key
AQS_EMAIL = open('aqs_email.txt').read().strip()
AQS_KEY = open('aqs_key.txt').read().strip()

# %%
# Get code for each state/territory
pl.DataFrame(requests.get(f'https://aqs.epa.gov/data/api/list/states?email={AQS_EMAIL}&key={AQS_KEY}').json()['Data'])

# %%
NEW_YORK_STATE_CODE = '36'

# %%
# Get code for each county in a given state/territory
pl.DataFrame(
    requests.get(f'https://aqs.epa.gov/data/api/list/countiesByState?email={AQS_EMAIL}&key={AQS_KEY}&state={NEW_YORK_STATE_CODE}')
    .json()['Data'])

# %%
# Brooklyn is Kings county
BROOKLYN_COUNTY_CODE = '047'

# %%
# Get code for each site in a given county
pl.DataFrame(requests.get(
    f'https://aqs.epa.gov/data/api/list/sitesByCounty?email={AQS_EMAIL}&key={AQS_KEY}'
    f'&state={NEW_YORK_STATE_CODE}&county={BROOKLYN_COUNTY_CODE}').json()['Data'])

# %%
JHS_126_SITE_CODE = '0122'
YEAR = '2022'

# "PM 2.5" and "Acceptable PM 2.5" are two different AQI indicators that can appear.
# PM 2.5 means the data was collected using a standardized sensor setup ("Federal Reference Method" aka FRM).
# "Acceptable PM 2.5" means the data was collected using a different method that is reasonably close to
# what the standard sensor would produce.
# See https://www.epa.gov/aqs/aqs-memos-technical-note-reporting-pm25-continuous-monitoring-and-speciation-data-air-quality
PM2_5_CODE = '88101'
PM2_5_ACC_CODE = '88502'

# %%
# Get summary of data for given site
df = pl.DataFrame(requests.get(
    f'https://aqs.epa.gov/data/api/annualData/bySite?email={AQS_EMAIL}&key={AQS_KEY}'
    f'&state={NEW_YORK_STATE_CODE}&county={BROOKLYN_COUNTY_CODE}&site={JHS_126_SITE_CODE}'
    f'&bdate={YEAR}0101&edate={YEAR}0101&param={PM2_5_CODE},{PM2_5_ACC_CODE}').json()['Data'])
pl.Config.set_tbl_rows(-1)
df.filter(pl.col('pollutant_standard') == 'PM25 24-hour 2024').transpose(include_header=True)
