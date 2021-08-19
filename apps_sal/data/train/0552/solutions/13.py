for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    items = list(map(int, input().split()))
    items.sort()
    v1 = abs(sum(items[k:]) - sum(items[:k]))
    items.sort(reverse=True)
    v2 = abs(sum(items[k:]) - sum(items[:k]))
    print(max(v1, v2))
