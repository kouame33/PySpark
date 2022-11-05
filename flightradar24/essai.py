from FlightRadar24.api import FlightRadar24API
import pandas as pd
import json
fr_api = FlightRadar24API()
airports = fr_api.get_airports()
airlines = fr_api.get_airlines()
flights = fr_api.get_flights()
zones = fr_api.get_zones()
#print(airports)
path='./data/'
print(path)
data_airports = pd.DataFrame(airports)
print(type(flights))
data_airports.to_parquet(path + 'airports.parquet', engine='fastparquet')

# Flights data
data_flights = pd.DataFrame(flights)
data_flights.to_csv(path + 'fli.csv')
print(data_flights)