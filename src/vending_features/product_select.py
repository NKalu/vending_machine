
class ProductSelect(object):
    def __init__(self):
        self.product_options = {
            'cola': 100,
            'chips': 50,
            'candy': 65
        }
        self.price_needed = 0
        self.product_selected = None
        super().__init__()
    
    def select_product(self, product: str):
        if product in self.product_options:
            self.price_needed = self.product_options[product]
            self.product_selected = product
    
    def deselect_product(self):
        self.price_needed = 0
        self.product_selected = None