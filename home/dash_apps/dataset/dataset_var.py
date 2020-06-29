import pandas as pd
from zipfile import ZipFile


zip_file = ZipFile('novel-corona-virus-2019-dataset.zip')

f_table = pd.read_csv(zip_file.open('covid_19_data.csv'),
                      parse_dates=['ObservationDate'])

# preprocessing
# change column name ObservationDate = Date
f_table.rename(columns={'ObservationDate': 'Date'}, inplace=True)
# Cased initiation
cases = ['Confirmed', 'Deaths', 'Recovered', 'Active']

# Active Case = confirmed - deaths - recovered
f_table['Active'] = f_table['Confirmed'] - f_table['Deaths'] - f_table['Recovered']

# replacing Mainland china with just China
f_table['Country/Region'] = f_table['Country/Region'].replace('Mainland China', 'China')

# filling missing values
f_table[['Province/State']] = f_table[['Province/State']].fillna('')
f_table[cases] = f_table[cases].fillna(0)

# Change integre to Float
f_table[['Confirmed', 'Deaths', 'Recovered', 'Active']] = f_table[
    ['Confirmed', 'Deaths', 'Recovered', 'Active']].astype(int)

# Selecksi Tabel yg akan digunakan
# cases in the ships
ship = f_table[f_table['Province/State'].str.contains('Grand Princess') | f_table['Country/Region']
    .str.contains('Cruise Ship')]

# china and the row
china = f_table[f_table['Country/Region'] == 'China']
row = f_table[f_table['Country/Region'] != 'China']

# latest
f_latest = f_table[f_table['Date'] == max(f_table['Date'])].reset_index()
china_latest = f_latest[f_latest['Country/Region'] == 'China']
row_latest = f_latest[f_latest['Country/Region'] != 'China']

# latest condensed
f_latest_grouped = f_latest.groupby('Country/Region')[
    'Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
china_latest_grouped = china_latest.groupby('Province/State')[
    'Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
row_latest_grouped = row_latest.groupby('Country/Region')[
    'Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()


#--------------------------------------------------------------------------

US_latest = f_latest[f_latest['Country/Region']=='US'].reset_index()
US_latest = US_latest[['Date','Province/State', 'Country/Region', 'Confirmed', 'Deaths']]

#menggabungkan data dengan kode - untuk menampilkan pada peta
state_df = pd.read_csv('us-state-ansi-fips.csv')
state_df.columns = ['Province/State', 'st', 'stusps']

US_latest = pd.merge(US_latest, state_df, on=['Province/State'], how='inner')

US_latest_grouped = US_latest.groupby(['Province/State','stusps'])['Confirmed', 'Deaths'].sum().reset_index()

#--------------------------------------------------------------------------
brazil_latest = f_latest[f_latest['Country/Region']=='Brazil']

brazil_latest_grouped = brazil_latest.groupby('Province/State')['Confirmed', 'Deaths'].sum().reset_index()

#hilangkan nilai unknown
brazil_latest_grouped = brazil_latest_grouped[brazil_latest_grouped['Province/State']!='Unknown']

br_latest = brazil_latest.copy()
br_df = pd.read_csv('brazil_lat_long.csv')
br_latest = pd.merge(br_latest, br_df, on=['Province/State'], how='inner')
br_latest = br_latest[['Date','Province/State', 'Lat', 'Long', 'Confirmed', 'Deaths']]

#--------------------------------------------------------------------------

#menggabungkan data dengan kode - untuk menampilkan pada peta
ch_df = pd.read_csv('china_lat_long.csv')
ch_df.head()

ch_latest = pd.merge(china_latest, ch_df, on=['Province/State'], how='inner')

ch_latest_grouped = ch_latest.groupby(['Province/State', 'Lat', 'Long'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()

