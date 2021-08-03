l = []
n = int(input())
for i in range(n):
    l.append(list(map(int, input().split())))
if(n == 1):
    print(1)
else:
    c = 2
    for i in range(1, n - 1):
        if(l[i][0] - l[i][1] > l[i - 1][0]):
            c = c + 1
        elif(l[i][0] + l[i][1] < l[i + 1][0]):
            l[i][0] += l[i][1]
            c = c + 1
    print(c)
