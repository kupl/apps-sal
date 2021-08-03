N, T = map(int, input().split())

r = [0] * (N + 1)
c = [0] * (N + 1)
for i in range(T):
    task = input().split()
    if(task[0] == "RowAdd"):
        r[int(task[1])] += int(task[2])
    if(task[0] == "ColAdd"):
        c[int(task[1])] += int(task[2])
print(max(r) + max(c))
