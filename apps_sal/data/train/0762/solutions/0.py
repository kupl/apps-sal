t = int(input())
while(t):
    n = int(input())
    cnt = 1
    for i in range(n):
        s = ""
        for j in range(n):
            s = s + str(bin(cnt))[2:][:: -1] + " "
            cnt = cnt + 1
        print(s)

    t = t - 1
