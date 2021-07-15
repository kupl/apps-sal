def order_weight(strng):
    strng = [list(map(int, i)) for i in strng.split(' ')]
    strng = sorted(sorted(strng), key=lambda num: sum(num))
    strng = ' '.join([''.join(map(str, i)) for i in strng])
    return strng
