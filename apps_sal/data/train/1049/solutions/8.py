for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = len(set(a))
    m = []
    for i in range(n - k + 2):
        if b == len(set(a[i:i + k])):
            m.append(sum(a[i:i + k]))
    print(max(m))
