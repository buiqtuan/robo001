# trade_orders.py
from datetime import datetime

class TradeOrders:
    def __init__(self, mt5):
        self.mt5 = mt5

    def order_check(self, request):
        result = self.mt5.order_check(request)
        return result

    def open_buy_order(self, symbol, volume, deviation):
        request = {
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": self.mt5.ORDER_TYPE_BUY,
            "price": self.mt5.symbol_info_tick(symbol).ask,
            "deviation": deviation,
            "magic": 234000,
            "comment": "opened by python",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_IOC,
        }
        result = self.mt5.order_send(request)
        return result

    def close_buy_order(self, ticket, volume, deviation):
        position_id=ticket
        request={
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": self.mt5.positions_get(ticket=position_id)[0].symbol,
            "volume": volume,
            "type": self.mt5.ORDER_TYPE_SELL,
            "position": position_id,
            "price": self.mt5.symbol_info_tick(self.mt5.positions_get(ticket=position_id)[0].symbol).bid,
            "deviation": deviation,
            "magic": 234000,
            "comment": "closed by python",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_IOC,
        }
        result = self.mt5.order_send(request)
        return result

    def open_sell_order(self, symbol, volume, deviation):
        request = {
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": self.mt5.ORDER_TYPE_SELL,
            "price": self.mt5.symbol_info_tick(symbol).bid,
            "deviation": deviation,
            "magic": 234000,
            "comment": "opened by python",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_IOC,
        }
        result = self.mt5.order_send(request)
        return result

    def close_sell_order(self, ticket, volume, deviation):
        position_id=ticket
        request={
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": self.mt5.positions_get(ticket=position_id)[0].symbol,
            "volume": volume,
            "type": self.mt5.ORDER_TYPE_BUY,
            "position": position_id,
            "price": self.mt5.symbol_info_tick(self.mt5.positions_get(ticket=position_id)[0].symbol).ask,
            "deviation": deviation,
            "magic": 234000,
            "comment": "closed by python",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_IOC,
        }
        result = self.mt5.order_send(request)
        return result