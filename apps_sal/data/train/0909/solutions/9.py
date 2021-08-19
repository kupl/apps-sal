T = int(input())
for _ in range(T):
    n = int(input())
    b = list(map(int, input().split()))
    g = list(map(int, input().split()))
    my_list = b + g
    my_list.sort()
    b1 = b.copy()
    g1 = g.copy()
    lim = 2 * n
    (k1, k2) = (1, 1)
    for i in range(lim):
        if my_list[i] in b and i % 2 == 0:
            b.remove(my_list[i])
        elif my_list[i] in g and i % 2:
            g.remove(my_list[i])
        else:
            k1 = 0
            break
    for i in range(lim):
        if my_list[i] in g1 and i % 2 == 0:
            g1.remove(my_list[i])
        elif my_list[i] in b1 and i % 2:
            b1.remove(my_list[i])
        else:
            k2 = 0
            break
    if k1 or k2:
        print('YES')
    else:
        print('NO')
