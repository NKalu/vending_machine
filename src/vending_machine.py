from src.vending_features.product_select import ProductSelect
from src.vending_features.coin_accept import CoinAcceptor

class VendingMachine(object):
    def __init__(self):
        self.coin_accept = CoinAcceptor()
        self.product_select = ProductSelect()
        super().__init__()

    def is_product_dispensed(self) -> bool:
        if self.product_select.product_selected:
            if self.product_select.price_needed <= self.coin_accept.coin_value:
                print(f"Dispensing {self.product_select.product_selected}")
                self.coin_accept.clear_coins()
                self.product_select.deselect_product()
                return True
        return False

    def vending_display(self) -> str:
        dispensed = self.is_product_dispensed()
        if dispensed:
            return "THANK YOU"
        elif self.coin_accept.number_of_coins:
            if self.product_select.product_selected:
                if self.coin_accept.coin_value < self.product_select.price_needed:
                    return f"PRICE ${self.product_select.price_needed - self.coin_accept.coin_value:.2f}"
            else:
                return f"${self.coin_accept.coin_value:.2f}"
        return "INSERT COIN"