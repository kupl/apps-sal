t = int(input())
while(t != 0):
    s = ''
    k = int(input())
    for i in range(1, k + 1):
        for j in range(i * (i + 1) // 2, i * (i - 1) // 2, -1):
            s = s + str(j)
        print(s)
        s = ''
    t -= 1
