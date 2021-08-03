import re


class Checkout(object):
    def __init__(self, d={}):
        self.pricing, self.total, self.fruits, self.free = d, 0, {}, {}

    def scan(self, n, qty=1):
        item = get_price(n)
        for i in range(qty):
            if not self.free.get(n, 0):
                self.total += item
                self.fruits[n] = self.fruits.get(n, 0) + 1
            else:
                self.free[n] -= 1
                continue
            if n in self.pricing:
                m = self.pricing[n]
                if 'for' in m:
                    how, f = m.split("for")
                    if not self.fruits[n] % int(how):
                        self.total = self.total - item * int(how) + float(f)
                elif 'buy' in m:
                    how, f = re.sub(r'buy|get', ' ', m).strip().split()
                    if not self.fruits[n] % int(how):
                        self.free[n] = int(f)
                elif 'off' in m:
                    how, f = re.sub(r'off|ormore', ' ', m).strip().split()
                    if self.fruits[n] == int(f):
                        self.total -= float(how)
            self.total = round(self.total, 2)
