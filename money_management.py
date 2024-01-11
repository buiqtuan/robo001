
# money_management.py
class MoneyManagement:
    def __init__(self, mt5, risk_per_trade, leverage):
        self.mt5 = mt5
        self.risk_per_trade = risk_per_trade
        self.leverage = leverage

    def calculate_volume(self, balance, stop_loss_pips, pip_value):
        risk_amount = balance * self.risk_per_trade
        volume = risk_amount / (stop_loss_pips * pip_value)
        return volume

    def place_order_with_sl_tp(self, symbol, order_type, volume, stop_loss, take_profit):
        request = {
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "price": self.mt5.symbol_info_tick(symbol).ask if order_type == self.mt5.ORDER_TYPE_BUY else self.mt5.symbol_info_tick(symbol).bid,
            "sl": stop_loss,
            "tp": take_profit,
            "deviation": 20,
            "magic": 234000,
            "comment": "opened by python",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_IOC,
        }
        result = self.mt5.order_send(request)
        return result