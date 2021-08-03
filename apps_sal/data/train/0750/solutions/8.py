t = int(input())
while t != 0:
    l = list(map(int, input().split()))
    l1 = [0] * len(l)
    for i in range(len(l)):
        l1[l[i] - 1] = i + 1
    if l1 == l:
        print('ambiguous')
    else:
        print('not ambiguous')
    t = int(input())
