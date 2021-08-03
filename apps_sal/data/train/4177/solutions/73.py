def men_from_boys(arr):
    man = []
    boy = []
    for x in set(arr):
        if x % 2 == 0:
            man.append(x)
        if x % 2 == 1:
            boy.append(x)
    return sorted(man) + sorted(boy, reverse=True)
