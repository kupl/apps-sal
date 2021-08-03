from operator import itemgetter


def top3(products, amounts, prices):
    zipped = zip(products, amounts, prices)
    revenues = list((product, amount * price) for product, amount, price in zipped)
    revenues.sort(key=itemgetter(1), reverse=True)
    return [product for product, revenue in revenues][:3]
