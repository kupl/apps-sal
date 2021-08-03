def Testcase():
    h, x, y = [int(x) for x in input().strip().split()]

    h = h - 1
    yt = h // y + 1
    # print(yt)
    flag = 0
    ans = 100000000009

    for i in range(0, yt):
        temp = x + i * y
        if h % temp == 0:
            flag = 1
            cl = i + int(h / temp)
            # print(temp,cl)
            ans = min(ans, cl)
            # print(temp,ans,i)
    print(ans if flag == 1 else '-1')


t = int(input())
while t > 0:
    Testcase()

    t -= 1
