from collections import Counter
ll = int(input())
n = list(map(int, input().rstrip().split(' ')))
l = Counter(n)
lst = []
for (i, j) in l.items():
    if j % 2 == 0:
        lst.append(j // 2)
    else:
        lst.append(j // 2 + 1)
print(sum(lst))
