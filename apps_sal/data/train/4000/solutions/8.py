from math import factorial as f


def strong_num(n):
    c = sum(map(lambda _: f(_), (int(i) for i in str(n)))) == n
    return 'STRONG!!!!' if c else 'Not Strong !!'
