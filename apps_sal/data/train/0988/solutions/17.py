t = int(input())
while (t > 0):
    n = int(input())
    x = list(map(int, input().split()))
    max = []
    for i in x:
        li = []
        for j in x:
            li.append(i ^ j)
        max.append(sum(li))
    print(min(max))
    t = t - 1
