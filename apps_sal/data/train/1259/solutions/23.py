# cook your dish here
t = int(input())
for i in range(t):
    c = 0
    l, r = list(map(int, input().split()))
    # print(c)
    for i in range(l, r + 1, 1):
        if(i % 10 == 2 or i % 10 == 3 or i % 10 == 9):
            c += 1
    print(c)
