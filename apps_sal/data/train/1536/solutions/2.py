from collections import Counter


def new_seq(l, d, x):
    new = [x]
    for i in range(len(l) - 1):
        t = new[-1] + d
        new.append(t)
    return new


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    aux = []
    for i in range(n - 1):
        aux.append(l[i + 1] - l[i])
    aux_1 = Counter(aux)
    aux = list(set(aux))
    if len(aux) > 1 and len(aux) == 3:
        a, b, c = aux[0], aux[1], aux[2]
        if a + b == (2 * c):
            t_1 = new_seq(l, c, l[0])
            print(*t_1)
        elif a + c == (2 * b):
            t_1 = new_seq(l, b, l[0])
            print(*t_1)
        else:
            t_1 = new_seq(l, a, l[0])
            print(*t_1)
    elif len(aux) == 2:
        t_2 = aux_1.most_common(1)[0][0]
        if l[0] - l[1] != t_2:
            print(*new_seq(l, t_2, l[1] - t_2))
        else:
            print(*new_seq(l, t_2, l[0]))
    else:
        print(*l)
