t = int(input())
for _ in range(t):
    n, p, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in a:
        if(i % 2 == 0):
            if(q >= i // 2):
                count += 1
                q -= i // 2
            else:
                if(p >= i - q - q):
                    count += 1
                    p -= i - q - q
                    q = 0
                else:
                    break
        else:
            if(q >= i // 2 and p > 0):
                count += 1
                p -= 1
                q -= i // 2
            else:
                if(p >= i - q - q):
                    count += 1
                    p -= i - q - q
                    q = 0
                else:
                    break
    print(count)
