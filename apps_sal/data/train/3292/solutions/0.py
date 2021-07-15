def calc(s):
    total1 = ''.join(map(lambda c: str(ord(c)), s))
    total2 = total1.replace('7', '1')
    return sum(map(int, total1)) - sum(map(int, total2))
