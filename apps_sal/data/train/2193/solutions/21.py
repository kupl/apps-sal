n = int(input())
u = []
t = 0
for i in range(n):
    u.append(sum(list(map(int, input().split()))))
t = u[0]
u.sort(reverse=1)
for i in range(n):
    if u[i] == t:
        print(i + 1)
        break
