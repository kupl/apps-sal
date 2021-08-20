def solve(a):
    (l1, l2) = ([], [])
    printed = False
    dic = dict.fromkeys(a, 0)
    for i in a:
        dic[i] += 1
        if dic[i] == 1:
            l1.append(i)
        if dic[i] == 2:
            l2.append(i)
        if dic[i] == 3:
            print('NO')
            return
            printed = True
            break
    if not printed:
        if max(l1) in l2:
            print('NO')
            return
        else:
            print('YES')
            l1 = sorted(l1)
            l2 = sorted(l2, reverse=True)
            print(*l1 + l2)


t = int(input())
while t:
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    solve(a)
