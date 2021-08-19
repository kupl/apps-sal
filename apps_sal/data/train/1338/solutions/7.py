t = list(map(float, input().split()))
i = 1
while i < len(t):
    num1 = t[i]
    num2 = t[i + 1]
    poww = 10 ** num2
    ans = num1 * poww
    print('%.2f' % ans)
    i += 2
