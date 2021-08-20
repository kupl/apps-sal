def super_size(n):
    nn = str(n)
    num = []
    for i in nn:
        num.append(int(i))
    numnum = sorted(num)
    numnum.reverse()
    for i in numnum:
        return int(''.join((str(i) for i in numnum)))
