t = eval(input())
for qq in range(t):
    n, m = list(map(int, input().split()))
    count = 0
    xmin, xmax, ymin, ymax = n + 1, -1, m + 1, -1
    for i in range(n):
        s = input()
        for j in range(m):
            if s[j] == "*":
                count += 1
                if i < xmin:
                    xmin = i
                else:
                    if i > xmax:
                        xmax = i
                if j < ymin:
                    ymin = j
                else:
                    if j > ymax:
                        ymax = j
    if count == 0:
        print(0)
    else:
        if count == 1:
            print(1)
        else:
            num = max((xmax - xmin), (ymax - ymin))
            if num & 1 == 0:
                print((num / 2) + 1)
            else:
                print((num / 2) + 2)
