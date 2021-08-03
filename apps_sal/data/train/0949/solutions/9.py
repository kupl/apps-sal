# cook your dish here
x = int(input())
for i in range(x):
    y = int(input())
    z = list(map(int, input().strip().split(" ")))
    m = 0
    for j in range(0, len(z)):
        t = j
        c = 0
        while((t + 1 < len(z) and z[t + 1] == z[t]) or (t + 2 < len(z) and z[t + 2] == z[t])):
            if(z[t + 1] == z[t]):
                t = t + 1
                c = c + 1
            else:
                t = t + 2
                c = c + 1
            if(c > m):
                m = c
    print(m)
