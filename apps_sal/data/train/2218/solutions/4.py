n = int(input())
a = list(map(int, input().split()))
q = int(input())

last_set = [0] * n
alles = [0]

for i in range(q):
    r = list(map(int, input().split()))
    if len(r) == 2:
        alles.append(r[1])
    else:
        last_set[r[1]-1] = len(alles)
        a[r[1]-1] = r[2]
        
maxis = alles
i = len(maxis) -1 
prev_max = 0
while i >= 0:
    prev_max = max(prev_max, alles[i])
    maxis[i] = prev_max
    i -= 1
    
for i in range(n):
    if last_set[i] < len(maxis):
        a[i] = max(a[i], maxis[last_set[i]])
    
print(" ".join(map(str, a)))

