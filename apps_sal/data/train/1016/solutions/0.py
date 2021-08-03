# cook your dish here
for t in range(int(input())):
    c = 0
    for i in range(int(input())):
        s, j = list(map(int, input().split()))
        if (j - s) > 5:
            c += 1
    print(c)
