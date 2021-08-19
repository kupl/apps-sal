t = list(map(float, input().split()))
i = 1
while i <= int(2 * t[0]):
    ans = t[i] * pow(10, t[i + 1])
    print('{:.2f}'.format(ans))
    i += 2
