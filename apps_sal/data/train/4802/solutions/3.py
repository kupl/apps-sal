import re


class Checkout(object):
    ip = {'onion': 0.99, 'leek': 2.99, 'apple': 0.4, 'orange': 0.75, 'tart': 5, 'potato': 0.8, 'rice': 1.1, 'carrot': 0.25, 'celery': 1.2}

    def __init__(self, promos={}):
        self.ci = []
        self.promo_ci = []
        self.ormore = []
        self.promos = promos
        print(promos)

    def extract_quant_doll(self, promo):
        (x, y) = (promo.split('for')[0], promo.split('for')[-1])
        try:
            x = int(x)
            y = float(y)
            return (x, y, 'for')
        except:
            try:
                spromo = promo.split('buy')[1]
                spromo = spromo.split('get')
                (x, y) = (spromo[0], spromo[-1])
                if x.isdigit() and y.isdigit():
                    return (int(x), int(y), 'buy')
            except:
                spromo = promo.split('off')
                x = float(spromo[0])
                spromo = spromo[-1]
                y = spromo.split('ormore')[0]
                y = int(y)
                return (y, x, 'ormore')

    def scan(self, item, nitems=1):
        print((item, nitems))
        price = self.get_price(item)
        i = 0
        while i < nitems:
            i += 1
            print((i, nitems))
            self.ci.append((item, price))
            if item in self.promos:
                xfory = self.promos[item]
                (quant, doll, type) = self.extract_quant_doll(xfory)
                if type == 'for':
                    count_items = len([x for x in self.ci if x[0] == item])
                    print(('for', quant, doll, item, self.ci, count_items))
                    if quant == count_items:
                        self.ci = [x for x in self.ci if x[0] != item]
                        self.promo_ci.append((item, doll))
                elif type == 'buy':
                    items_sofar = [x for x in self.ci if x[0] == item]
                    price_total = sum([x[1] for x in items_sofar])
                    count_items = len(items_sofar)
                    print(('get', quant, doll, item, self.ci, count_items))
                    if quant + doll == count_items:
                        self.ci = [x for x in self.ci if x[0] != item]
                        self.promo_ci.append((item, quant * self.get_price(item)))
                elif type == 'ormore':
                    if item not in self.ormore:
                        items_sofar = [x for x in self.ci if x[0] == item]
                        price_total = sum([x[1] for x in items_sofar])
                        count_items = len(items_sofar)
                        print(('ormore', quant, doll, item, self.ci, count_items))
                        if count_items >= quant:
                            self.promo_ci.append((item, -doll))
                            self.ormore.append(item)

    def get_price(self, item):
        return self.ip.get(item, 0)

    @property
    def total(self):
        total_prices = [x[1] for x in self.ci]
        total_promos = [x[1] for x in self.promo_ci]
        print((self.ci, self.promo_ci))
        total_sum = sum(total_prices) if self.ci != [] else 0.0
        total_sum += sum(total_promos) if self.promo_ci != [] else 0.0
        return total_sum
