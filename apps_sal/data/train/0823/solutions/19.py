from itertools import combinations
for _ in range(int(input())):
    l = list(map(int, input().split()))
    c = 0
    for i in range(1, 5):
        if c:
            break
        a = list(combinations(l, i))
        for j in a:
            if sum(j) == 0:
                c = 1
                break
    if c:
        print('Yes')
    else:
        print('No')
