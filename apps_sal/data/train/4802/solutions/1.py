from collections import defaultdict


class Checkout(object):
    prices = {"onion": 0.99, "leek": 2.99, "apple": 0.40,
              "orange": 0.75, "tart": 5.00, "potato": 0.80,
              "rice": 1.10, "carrot": 0.25, "celery": 1.20}

    def __init__(self, sale=None):
        self.sale = sale if sale else {}
        self.count = defaultdict(int)

    def scan(self, s, x=1):
        self.count[s] += x

    @property
    def total(self):
        res = 0
        for k, v in self.count.items():
            s = self.sale.get(k, '')
            if 'for' in s:
                x, y = map(float, s.split('for'))
                q, v = divmod(v, x)
                res += q * y
            elif 'buy' in s:
                x, y = map(int, s[3:].split('get'))
                v -= v // (x + y)
            elif 'off' in s:
                x, y = map(float, s[:-6].split('off'))
                if v >= y:
                    res -= x
            res += v * Checkout.prices[k]
        return res
