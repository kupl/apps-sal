def run(i):
    nonlocal l
    d[i] = 1
    if(l[i][1] == 0):
        return i
    return run(l[i][1])


n = int(input())
l = []
for u in range(n):
    l.append(list(map(int, input().split())))
l.insert(0, 0)
d = {}
ans = 0
start = 0
for i in range(1, len(l)):
    if(l[i][0] == 0):
        ans = run(i)
        start = i
        break
for i in range(start + 1, len(l)):
    if(l[i][0] == 0):
        l[i][0] = ans
        l[ans][1] = i
        ans = run(i)
for val in range(1, len(l)):
    print(l[val][0], l[val][1])
