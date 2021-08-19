for i in range(int(input())):
    (n, d) = map(int, input().split())
    l = list(map(int, input().split()))
    if n == d:
        print(n)
    else:
        count = 0
        risk = []
        for i in l:
            if i >= 80 or i <= 9:
                risk.append(i)
        count += len(risk) // d
        if len(risk) % d < d and len(risk) % d > 0:
            count += 1
        k = len(l) - len(risk)
        count += k // d
        if k % d > 0 and k % d < d:
            count += 1
        print(count)
