def sumStr(strng):
    return sum(int(num) for num in strng)


def order_weight(strng):
    strList = sorted(strng.split(' '))
    return ' '.join(sorted(strList, key=sumStr))
