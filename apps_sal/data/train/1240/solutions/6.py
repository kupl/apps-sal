# cook your dish here
t = int(input())
for i in range(0, t):
    n = int(input())
    s = 0
    l = list(map(int, input().split()))
    for j in l:
        if(j % 6 == 0):
            s += 6
        else:
            r = j % 6
            s += r
    print(s)
