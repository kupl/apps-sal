# A blank slate
class Checkout:
    items = {
        "onion": 0.99, 
        "leek": 2.99,
        "apple": 0.4,
        "orange": 0.75,
        "tart": 5.0,
        "potato": 0.8,
        "rice": 1.1,
        "carrot": 0.25,
        "celery": 1.2,
    }
    
    def __init__(self, deals=None):
        self.scanned = []
        self.deals = deals or {}
        
    def scan(self, item, count=1):
        self.scanned.extend([item]*count)
    
    @property
    def total(self):
        total = 0
        for item, deal in self.deals.items():
            if item in self.scanned:
                item_count = self.scanned.count(item)
                if "for" in deal:
                    count, price = deal.split("for")
                    a, b = divmod(item_count, int(count))
                    total += a * float(price) + b * self.items[item]
                elif "buy" in deal:
                    count, free = deal[3:].split("get")
                    a, b = divmod(item_count, int(count) + int(free))
                    total += (item_count - a * int(free)) * self.items[item]
                elif "off" in deal:
                    discount, threshold = deal[:-6].split("off")
                    total += item_count * self.items[item]
                    if item_count >= int(threshold):
                        total -= float(discount)
        total += sum(self.items[i] for i in self.scanned if i not in self.deals)
        return total
