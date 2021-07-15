from collections import Counter
import re

class Checkout(object):
    def __init__(self, offers={}):
        self.purchased = Counter() 
        self.offers = {'for': {}, 'get': {}, 'off': {}}
        for k, v in offers.items():
            if 'for' in v:
                qty, price = v.split('for')
                self.offers['for'][k] = (int(qty), float(price))
            if 'get' in v:
                r = re.findall(r'\d+', v)
                self.offers['get'][k] = (int(r[0]), int(r[1]))
            if 'off' in v:
                r = re.findall(r'\d+\.\d+|\d+', v)
                self.offers['off'][k] = (float(r[0]), int(r[1]))
    
    @property
    def total(self):
        ans = 0.0
        for k, v in self.purchased.items():
            if k in self.offers['for']:
                q, r = divmod(v, self.offers['for'][k][0])
                ans += self.offers['for'][k][1] * q
                v = r
            if k in self.offers['get']:
                q, r = divmod(v, sum(self.offers['get'][k]))
                ans += get_price(k) * q * self.offers['get'][k][0]
                v = r
            if k in self.offers['off']:
                if v >= self.offers['off'][k][1]:
                    ans -= self.offers['off'][k][0]
            ans += get_price(k) * v
        return ans

    def scan(self, item, qty=1):
        self.purchased[item] += qty
