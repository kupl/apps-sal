instr = input()
tmplist = instr.split()
n = int(tmplist[0])
lx = [n for i in range(n)]
ly = [n for i in range(n)]
m = int(tmplist[1])
for i in range(m):
    instr = input()
    tmplist = instr.split()
    x = int(tmplist[0])
    y = int(tmplist[1])
    lx[x - 1] -= 1
    ly[y - 1] -= 1
ans = 0
for i in range(1, n - 1):
    if lx[i] == n:
        ans += 1
    if ly[i] == n:
        ans += 1
if n % 2 == 1:
    if lx[n // 2] == n and ly[n // 2] == n:
        ans -= 1
print(ans)
