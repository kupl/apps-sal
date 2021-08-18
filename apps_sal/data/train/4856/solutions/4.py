def adjust(coin, price):
    residue = price % coin
    if residue:
        price += coin - residue
    return price
