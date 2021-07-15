from collections import Counter

for t in range(int(input())):
    n = int(input())
    pos = [(i, input().strip().find('1')) for i in range(n)]
    c = n
    for i in range(2, n + 1):
        multiset = Counter()
        for k in range(i):
            multiset[pos[k][0]] += 1
            multiset[pos[k][1]] += 1
        if len(multiset) == i:
            c += 1
        for j in range(1, n - i + 1):
            multiset[pos[j - 1][0]] -= 1
            if multiset[pos[j - 1][0]] == 0:
                del multiset[pos[j - 1][0]]
            multiset[pos[j - 1][1]] -= 1
            if multiset[pos[j - 1][1]] == 0:
                del multiset[pos[j - 1][1]]
            multiset[pos[j + i - 1][0]] += 1
            multiset[pos[j + i - 1][1]] += 1
            if len(multiset) == i:
                c += 1
    print(c)

