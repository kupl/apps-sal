# cook your dish here
t = int(input())
while (t > 0):
    t -= 1
    n = int(input())
    count = 0
    list = []
    for i in range(n):
        list.append([int(x) for x in input().split()])
    for d in range(n - 1, 0, -1):
        result = list[d][d - 1] + 1
        if result != list[d][d]:
            count += 1
            next = d + 1
            for i in range(next):
                for j in range(i, next):
                    temp = list[i][j]
                    list[i][j] = list[j][i]
                    list[j][i] = temp
    print(count)
