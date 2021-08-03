t = int(input())
for _ in range(t):
    nkd = list(map(int, input().split()))
    k = nkd[1]
    d = nkd[2]
    an = list(map(int, input().split()))
    sum1 = sum(an)
    if sum1 < k:
        print("0")
    else:
        a = sum1 // k
        if a > d:
            print(d)
        else:
            print(a)
