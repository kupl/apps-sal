def factors(x):
    result = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            result.append(i)
            if x // i != i:
                result.append(x // i)
        i += 1
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = factors(n)
    an = -1
    for i in a:
        c = ((i * k * (k + 1)) // 2)
        if (c % i == 0 and c <= n):
            an = max(an, i)
    print(an)
