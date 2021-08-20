li = input().split()
for i in range(1, len(li), 2):
    k = float(li[i])
    m = int(li[i + 1])
    s = pow(10, m)
    ans = format(k * s, '.2f')
    print(ans)
