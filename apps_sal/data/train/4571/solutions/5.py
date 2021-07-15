from math import log

def decompose(num):
    ns = []
    for i in range(2, 100):
        j = int(log(num or 1, i))
        if j <= 1:
            break
        ns.append(j)
        num -= i ** j
    return [ns, num]
