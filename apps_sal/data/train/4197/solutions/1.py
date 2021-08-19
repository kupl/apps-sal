import heapq


def top3(products, amounts, prices):
    items = zip(products, amounts, prices)
    return [product for (product, _, _) in heapq.nlargest(3, items, key=lambda item: item[1] * item[2])]
