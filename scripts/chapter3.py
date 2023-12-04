# Chapter 3

import configparser
import quandl as q
from chapter3_scripts import generate_sample_data

config = configparser.ConfigParser()
config.read('../config/pyalgo.cfg')

def print_eod_quandl():
    # Reads historical data for the BTC/USD exchange rate.
    data = q.get('BCHAIN/MKPRU', api_key=config['quandl']['api_key'])
    # Selects the Value column, resamples it—from the originally daily values to yearly values—and defines the last
    # available observation to be the relevant one.
    print(data['Value'].resample('A').last())

    eod_data = q.get('FSE/SAP_X', start_date='2018-1-1', end_date='2020-05-01', api_key=config['quandl']['api_key'])
    print(eod_data)

if "__main__" == __name__:
    response = input("Select qandl print with (1) or Eikon (2):")

    try:
        choice = int(response)
        if choice == 1:
            print_eod_quandl()
        if choice == 2:
            pass
    except:
        print(f"Invalid option {response}. Should be (1) or (2)")