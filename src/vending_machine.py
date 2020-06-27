from vending_features.product_select import ProductSelect
from vending_features.coin_accept import CoinAcceptor

class VendingMachine(object):
    self.coin_accept = CoinAcceptor()
    self.product_select = ProductSelect()

def vending_display(self, product_dispensed: bool=False) -> str:
    if product_dispensed:
        return "THANK YOU"
    if not self.product_select.product_selected:
        return "INSET COIN"
    if self.coin_accept.coin_value < self.product_select.price_needed:
        return f"PRICE {self.product_select.price_needed - self.coin_accept.coin_value}"
