from math import ceil
adjust = lambda coin, price: ceil(price / float(coin)) * coin
