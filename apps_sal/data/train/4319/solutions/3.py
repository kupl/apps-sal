D = {**{c: 1 for c in "abdegopq069DOPQR"},
     **{c: 2 for c in "%&B8"}}


def countzero(string):
    return sum(D.get(c, string[i:i + 2] == '()') for i, c in enumerate(string))
