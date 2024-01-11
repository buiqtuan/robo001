# data_import.py
from datetime import datetime
import pandas as pd

class DataImport:
    mt5 = None

    def __init__(self, mt5):
        self.mt5 = mt5

    # Import ticks data from a specific date
    def import_ticks_date(self, symbol, date):
        ticks = self.mt5.copy_ticks_from(symbol, date, 1000, self.mt5.COPY_TICKS_ALL)
        return ticks

    # Import ticks data from a specific range of dates
    def import_ticks_range(self, symbol, date_from, date_to):
        ticks = self.mt5.copy_ticks_range(symbol, date_from, date_to, self.mt5.COPY_TICKS_ALL)
        return ticks

    # Import candlesticks data from a specific date
    def import_candlesticks_date(self, symbol, date):
        rates = self.mt5.copy_rates_from(symbol, self.mt5.TIMEFRAME_D1, date, 1000)
        return rates

    # Import candlesticks data from a specific range of dates
    def import_candlesticks_range(self, symbol, date_from, date_to):
        rates = self.mt5.copy_rates_range(symbol, self.mt5.TIMEFRAME_D1, date_from, date_to)
        return rates
    
    def import_candlesticks_from_2003(self, symbol):
        start_time = datetime(2003, 1, 1)
        rates = self.mt5.copy_rates_from(symbol, self.mt5.TIMEFRAME_M1, start_time, 0)
        
        # Convert the returned tuple to a DataFrame
        rates_frame = pd.DataFrame(list(rates),
                                   columns=['time', 'open', 'high', 'low', 'close', 'tick_volume', 'spread', 'real_volume'])
        
        # Convert time in seconds into the datetime format
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

        # Format time as 'YYYYMMDD hh:mm:ss'
        # rates_frame['time'] = rates_frame['time'].dt.strftime('%Y%m%d %H:%M:%S')
        
        return rates_frame