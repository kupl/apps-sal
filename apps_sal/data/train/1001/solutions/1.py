t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split(" ")))
    count = 0
    for j in range(n):
        if(j == 0):
            count = count + 1
        else:
            lst = []
            if(j <= 5):
                for k in range(j):
                    lst.append(p[k])
            else:
                e = j - 5
                for k in range(e, j):
                    lst.append(p[k])
            if(p[j] < min(lst)):
                count = count + 1
    print(count)
