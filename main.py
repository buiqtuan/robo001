
# main.py
import MetaTrader5 as mt5

# Initialize the bound between MetaTrader 5 and Python.
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# Get last error.
last_error = mt5.last_error()
print("last_error: ",last_error)

# Extract account information.
account_info = mt5.account_info()
if account_info!=None:
    # print out account data as a list
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))

# Extract symbol information.
symbol_info = mt5.symbol_info("EURUSD")
if symbol_info!=None:
    # print out symbol data as a list
    print("Show symbol_info()._asdict():")
    symbol_info_dict = mt5.symbol_info()._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))

# Extract book orders.
book_info = mt5.symbol_info_tick("EURUSD")
if book_info!=None:
    # print out book info data as a list
    print("Show symbol_info_tick()._asdict():")
    book_info_dict = mt5.symbol_info_tick()._asdict()
    for prop in book_info_dict:
        print("  {}={}".format(prop, book_info_dict[prop]))

# Close the connection to MetaTrader 5
mt5.shutdown()