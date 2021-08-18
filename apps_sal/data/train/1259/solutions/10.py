t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = [2, 3, 9]
    d = 0
    for j in range(a, b + 1):
        if(j % 10 in c):
            d = d + 1
    print(d)
