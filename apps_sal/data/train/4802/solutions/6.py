class Checkout(object):
    def __init__(self, sale_codes={}):
        self.total = 0
        self.scanned_items = {}
        self.sale_codes = sale_codes

    def update_total(self):
        tot = 0

        for item, count in list(self.scanned_items.items()):
            if item in self.sale_codes:
                if self.sale_codes[item].startswith("buy"):
                    buy, get = [int(x) for x in self.sale_codes[item][3:].split("get")]
                    tot += (count // (buy + get)) * (buy * get_price(item))
                    tot += (count % (buy + get)) * get_price(item)
                elif "for" in self.sale_codes[item]:
                    sale_count, sale_for = [float(x) for x in self.sale_codes[item].split("for")]
                    tot += (count // sale_count) * sale_for
                    tot += (count % sale_count) * get_price(item)
                elif "ormore" in self.sale_codes[item]:
                    price_off, min_count = [float(x) for x in self.sale_codes[item][:-6].split("off")]
                    tot += count * get_price(item)
                    if count >= min_count:
                        tot += -price_off
            else:
                tot += get_price(item) * count

        self.total = tot

    def scan(self, item, quantity=1):
        if item not in self.scanned_items:
            self.scanned_items[item] = quantity
        else:
            self.scanned_items[item] += quantity

        self.update_total()
