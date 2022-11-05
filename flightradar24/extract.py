from FlightRadar24.api import FlightRadar24API
import pandas as pd
import json
import re

fr_api = FlightRadar24API()
airports = fr_api.get_airports()
airlines = fr_api.get_airlines()
flights = fr_api.get_flights()
print("merci moad")
'''
pattern = r'[< >]'
mod_string = re.sub(pattern, '', flights)
'''

ll=[s.strip().split('<') for s in flights]


zones = fr_api.get_zones()
print(ll)

print(type(flights))
path='./data/'

#Airports data
data_airports = pd.DataFrame(airports)
data_airports.to_parquet(path + 'airports.parquet', engine='fastparquet')

# Airlines data
data_airlines = pd.DataFrame(airlines)
data_airlines.to_parquet(path + 'airlines.parquet', engine='fastparquet')
'''
# Flights data
data_flights = pd.DataFrame(flights)
data_flights.to_parquet(path + 'flights.parquet', engine='fastparquet')

# Zones data

data_zones = pd.DataFrame(zones)
data_zones.to_parquet(path + 'zones.parquet', engine='fastparquet')
'''
print("------------------------airline----------------------------")

with open(path + 'zones.json', 'w') as outfile:
    json.dump(zones, outfile)
