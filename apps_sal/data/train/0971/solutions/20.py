from collections import Counter
T = int(input())
for i in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    count = Counter(lst)
    print(n - max(count.values()))
