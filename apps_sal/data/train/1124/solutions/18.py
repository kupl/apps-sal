t = int(input())
for _ in range(t):
    (n, p, q) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in a:
        if p == 0 and q == 0:
            break
        elif i % 2 == 0:
            if q >= i // 2:
                count += 1
                q -= i // 2
            elif p >= i - q - q:
                count += 1
                p -= i - q - q
                q = 0
            else:
                continue
        elif q >= i // 2 and p > 0:
            count += 1
            p -= 1
            q -= i // 2
        elif p > max(i - q - q, 0):
            count += 1
            p -= i - q - q
            q = 0
        else:
            continue
    print(count)
