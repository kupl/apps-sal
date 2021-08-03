t = int(input())
for _ in range(t):
    n = int(input())
    time = []
    l = dict()
    for __ in range(n):
        name = input()
        t = int(input())
        l[t] = name
        time.append(t)
    time.sort()
    for i in range(n):
        print(l[time[i]])
