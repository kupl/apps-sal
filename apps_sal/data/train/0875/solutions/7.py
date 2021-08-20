from collections import defaultdict
for t in range(int(input())):
    (n, z1, z2) = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    c = 0
    dic = defaultdict(int)
    for i in seq:
        dic[i] = 1
        dic[-i] = 1
    if dic[z1] or dic[z2]:
        print(1)
        continue
    for i in seq:
        if dic[z1 - i] or dic[z2 - i]:
            c += 1
        if dic[z1 + i] or dic[z2 + i]:
            c += 1
    if c == 2 * len(seq):
        print(2)
    else:
        print(0)
