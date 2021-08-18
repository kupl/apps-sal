
t = int(input())
for rep in range(t):
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        x = int(input())
        l.append([s, x])
    l.sort(key=lambda x: x[1])
    for j in l:
        print(j[0])
