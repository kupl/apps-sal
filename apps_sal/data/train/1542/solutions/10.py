# cook your dish here
t = int(input())
for i in range(0, t):
    n = int(input())
    s = str(input())
    l = list(map(int, input().split()))
    sum1 = sum(l)
    finalSum = 0
    for i in range(n - 7):
        sum2 = 0
        dw = 1
        tw = 1
        for k in range(i, i + 8):
            if s[k] == "d":
                sum2 = sum2 + 2 * l[k - i]
            elif s[k] == "t":
                sum2 = sum2 + 3 * l[k - i]
            elif s[k] == "D":
                dw *= 2
                sum2 = sum2 + l[k - i]
            elif s[k] == "T":
                tw *= 3
                sum2 = sum2 + l[k - i]
            else:
                sum2 = sum2 + l[k - i]

        # print(sum2)
        finalSum = max(finalSum, sum2 * dw * tw)

    print(finalSum)
