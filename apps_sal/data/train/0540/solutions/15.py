t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().strip().split()))
    list1 = list(map(int, input().strip().split()))
    count = list1.count(m)
    set1 = set(list1)
    list2 = list(set1)
    if len(list2) <= m - 2:
        print(-1)
    elif list2[m - 2] != m - 1:
        print(-1)
    else:
        print(n - count)
