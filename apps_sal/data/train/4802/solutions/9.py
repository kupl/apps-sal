from collections import defaultdict
import re


class Checkout():
    def __init__(self, deals={}):
        self.bought = defaultdict(int)
        self.deals = deals

    def scan(self, s, n=1):
        self.bought[s] += n

    @property
    def total(self):
        def calculate_price(k, v, deal):
            if deal == None:
                return get_price(k) * v
            elif re.match(r'^([\d\.]+)for([\d\.]+)$', deal):
                c, d = re.match(r'^([\d\.]+)for([\d\.]+)$', deal).groups()
                return float(d) * (v // int(c)) + get_price(k) * (v % int(c))
            elif re.match(r'^buy([\d\.]+)get([\d\.]+)$', deal):
                f, t = re.match(r'^buy([\d\.]+)get([\d\.]+)$', deal).groups()
                return get_price(k) * (v // (int(f) + int(t)) * int(f) + v % (int(f) + int(t)))
            elif re.match(r'^([\d\.]+)off([\d\.]+)ormore$', deal):
                d, c = re.match(r'^([\d\.]+)off([\d\.]+)ormore$', deal).groups()
                return get_price(k) * v - float(d) * (v >= int(c))
            else:
                return get_price(k) * v
        return sum(calculate_price(k, v, self.deals.get(k, None)) for k, v in self.bought.items())
