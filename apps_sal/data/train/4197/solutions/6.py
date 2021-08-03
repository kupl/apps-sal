def top3(products, amounts, prices):
    productObjects = []
    for p in range(0, len(products)):
        productObjects.append(Product(products[p], amounts[p], prices[p], p))
    top3Products = sorted(productObjects, key=lambda x: x.Revenue, reverse=True)[:3]
    if len(list(p.Revenue for p in top3Products)) != len(list(p.Revenue for p in top3Products)):
        return [x for _, x in zip(products, names)]
    return [p.Name for p in top3Products]


class Product():
    def __init__(self, name, amount, price, defaultIndex):
        self.Name = name
        self.Revenue = amount * price
        self.DefaultIndex = defaultIndex
