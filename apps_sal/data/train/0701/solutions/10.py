q = int(input())
for i in range(q):
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    po = [(m)**i for i in l]
    r = sum(po)
    l = 0
    count = 0
    max = 1
    for i in range(n):
        l += po[i]
        r -= po[i]
        p = l * r
        if p > max:
            max = p
            count += 1
    print(count)
