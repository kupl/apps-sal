from itertools import combinations
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    a = list(combinations(lst, 2))
    count = 0
    for i in range(len(a)):
        if sum(a[i]) % 2 != 0:
            count += 1
    print(count)
