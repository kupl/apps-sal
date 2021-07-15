from collections import Counter
from re import compile, fullmatch

class Checkout:
    offers = {
        compile('(\d+)for([.\d]+)'): lambda m: (lambda qty, price: qty // int(m[1]) * float(m[2]) + qty % int(m[1]) * price),
        compile('buy(\d+)get(\d+)'): lambda m: (lambda qty, price: (qty // (int(m[1]) + int(m[2])) * int(m[1]) + qty % (int(m[1]) + int(m[2]))) * price),
        compile('([.\d]+)off(\d+)ormore'): lambda m: (lambda qty, price: qty * price - float(m[1]) * (qty >= int(m[2]))),
    }

    def _parse_sale(self, sale):
        for offer, func in list(self.offers.items()):
            match = offer.fullmatch(sale)
            if match: return func(match)

    def __init__(self, sales=None):
        self.products = Counter()
        self.sales = {product: self._parse_sale(sale) for product, sale in list((sales or {}).items())}

    def scan(self, product, quantity=1):
        self.products[product] += quantity

    def calculate_cost(self, product):
        try:
            return self.sales[product](self.products[product], get_price(product))
        except KeyError:
            return self.products[product] * get_price(product)
        
    @property
    def total(self):
        return sum(self.calculate_cost(p) for p in self.products)

