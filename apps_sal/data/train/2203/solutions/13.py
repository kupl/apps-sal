n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
    p[i].sort()
    p[i].append(i)
p.sort()
pos = [0] * n
for i in range(n):
    pos[p[i][-1]] = i + 1
print(*pos)

    
    
        

