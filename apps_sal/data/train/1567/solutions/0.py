for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    for j in s:
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1
    f = 0
    for j in d:
        if(d[j] % 2 == 1):
            f = f + 1
    if((n // 2) % 2 == 0 and f == 0):
        print("YES")
        continue
    if((n // 2) % 2 == 1 and f <= 2 and f % 2 == 0):
        print("YES")
        continue
    print("NO")
