from src.vending_features.product_select import ProductSelect
from src.vending_features.coin_accept import CoinAcceptor

class VendingMachine(object):
    def __init__(self):
        self.coin_accept = CoinAcceptor()
        self.product_select = ProductSelect()
        self.change_in_machine = 100
        super().__init__()

    def is_product_dispensed(self) -> bool:
        # logic to dispense if product should be dispensed to customer
        if self.product_select.product_selected:
            if self.change_in_machine < 0.05:
                # if no change in the machince only take exact change
                if self.product_select.price_needed == self.coin_accept.coin_value:
                    print(f"Dispensing {self.product_select.product_selected[0]}")
                    self.coin_accept.clear_coins()
                    self.product_select.deselect_product()
                    return True
            else:
                if self.product_select.price_needed == self.coin_accept.coin_value:
                    print(f"Dispensing {self.product_select.product_selected[0]}")
                    self.coin_accept.clear_coins()
                    self.product_select.deselect_product()
                    return True
                elif self.product_select.price_needed < self.coin_accept.coin_value:
                    print(f"Dispensing {self.product_select.product_selected[0]}")
                    return_amount = ((self.coin_accept.coin_value - self.product_select.price_needed)*100) / 5
                    for x in range(return_amount):
                        self.coin_accept.coin_return('nickel')
                        self.change_in_machine -= .05
                    self.coin_accept.clear_coins()
                    self.product_select.deselect_product()
                    return True
        return False

    def vending_display(self) -> str:
        # the "display" that the user will see
        if not self.product_select.in_stock:
            self.product_select.deselect_product()
            return "SOLD OUT"
        standard_display = "INSERT COIN"
        # check to make sure there is enough change to dispense from machine
        if self.change_in_machine < 0.05:
            standard_display = "EXACT CHANGE ONLY"
        dispensed = self.is_product_dispensed()
        if dispensed:
            return "THANK YOU"
        elif self.coin_accept.number_of_coins:
            if self.product_select.product_selected:
                if self.coin_accept.coin_value < self.product_select.price_needed:
                    return f"PRICE ${self.product_select.price_needed - self.coin_accept.coin_value:.2f}"
            else:
                return f"${self.coin_accept.coin_value:.2f}"
        return standard_display