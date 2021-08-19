import itertools
(s, n, s1, lis, new1) = ([], [], [], [], [])
q = int(input())
s.append(input().split(' '))
s1 = list([list(map(int, x)) for x in s])
sum1 = sum(s1[0])
if len(s1) % 2 != 0:
    z = (len(s1[0]) + 1) // 2
    n = list(itertools.combinations(s1[0], z))
    for j in range(len(n)):
        x = sum(n[j])
        if x == sum1 // 2:
            lis = n[j]
            break
    new1 = list(lis)
    print(' '.join(map(str, new1)))
    for j in range(len(lis)):
        y = lis[j]
        s1[0].remove(y)
    print(' '.join(map(str, s1[0])))
else:
    z = len(s1[0]) // 2
    n = list(itertools.combinations(s1[0], z))
    for j in range(len(n)):
        x = sum(n[j])
        if x == sum1 // 2:
            lis = n[j]
            break
    new1 = list(lis)
    print(' '.join(map(str, new1)))
    for j in range(len(lis)):
        y = lis[j]
        s1[0].remove(y)
    print(' '.join(map(str, s1[0])))
