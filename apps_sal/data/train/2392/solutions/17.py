t = int(input())
for z in range(t):
    n, m = map(int, input().split())
    if m > n:
        print(0)
        continue
    use = []
    x = m
    for i in range(20):
        use.append(x % 10)
        x += m
    # print(use)
    arr = []
    for i in range(len(use)):
        if not use[i] in arr:
            arr.append(use[i])
        else:
            break

    l = len(arr)
    cnt = n // (l * m)
    left = (n % (l * m)) // m
    print(cnt * sum(arr) + sum(arr[:left]))
