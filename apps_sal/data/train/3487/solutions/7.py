def beeramid(bonus, price):
    if bonus < price:
        return 0
    elif bonus == price:
        return 1
    else:
        L = []
        a = int(bonus // price) + 1
        c = 1
        for i in range(1, a):
            c += i * i
            if c <= a:
                L.append(i * i)
        b = len(L)
        return b
