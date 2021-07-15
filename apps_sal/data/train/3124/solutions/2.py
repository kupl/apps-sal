from itertools import count

def get_exponent(n, p):
    if p > 1:
        for res in count():
            n, r = divmod(n, p)
            if r:
                return res
