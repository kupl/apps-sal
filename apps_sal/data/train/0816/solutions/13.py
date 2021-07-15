try:
    t = int(input())
    k = list(map(int, input().split()))
    p = int(input())
    for _ in range(p):
        h = int(input())
        print(k[h - 1])
        k.remove(k[h - 1])

except:
    pass

