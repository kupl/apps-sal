import math


def prime(aa):
    f = 0
    if aa >= 100:
        to = int(math.sqrt(aa))
    else:
        to = aa
    for y in range(2, to):
        if aa % y == 0:
            return 0
    return 1


te = int(input())
for _ in range(te):
    a = int(input())
    ar = []
    ar.append(2)
    f = 0
    c = 0
    pc = 3
    add = 0
    for x in ar:
        try:
            add = add + ar[x - 1]
        except:
            while True:
                if prime(pc) == 1:
                    ar.append(pc)
                    if x <= len(ar):
                        break
                pc += 1
            pc += 1
        add = add + ar[x - 1]
        c += 1
        if c == a:
            break
    print(add)
