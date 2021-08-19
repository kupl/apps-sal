# cook your dish here
x = int(input())
for m in range(x):
    y = int(input())
    l = list(map(int, input().split(" ")))
    count = 0
    for i in range(y - 1):
        f = l[i]
        for j in range(i + 1, y):
            f = f ^ l[j]
            if f == 0:
                count += j - i
    print(count)
