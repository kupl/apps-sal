for T in range(int(input())):
    import copy
    (n, d) = [abs(int(n)) for n in input().split()]
    lst = [abs(int(lst)) for lst in input().split()]
    cpy = copy.copy(lst)
    risk = []
    for item in lst:
        if item <= 9 or item >= 80:
            risk.append(item)
            cpy.remove(item)
    import math
    d1 = math.ceil(len(cpy) / d)
    d2 = math.ceil(len(risk) / d)
    print(d1 + d2)
