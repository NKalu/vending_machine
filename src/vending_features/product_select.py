
class ProductSelect(object):
    def __init__(self):
        self.product_options = {
            'cola': (1, True),
            'chips': (.5, True),
            'candy': (.65, True)
        }
        self.price_needed = 0
        self.product_selected = None
        self.in_stock = True
        super().__init__()
    
    def select_product(self, product: str):
        if product in self.product_options:
            self.price_needed = self.product_options[product][0]
            self.in_stock = self.product_options[product][1]
            self.product_selected = product
            
    
    def deselect_product(self):
        self.price_needed = 0
        self.product_selected = None
        self.in_stock = True