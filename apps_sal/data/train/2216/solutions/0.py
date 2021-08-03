import sys
s = sys.stdin.readline().split()[0]

m = int(sys.stdin.readline())

Numx = []
Numy = []
Numz = []
x = 0
y = 0
z = 0
for i in range(len(s)):
    if(s[i] == 'x'):
        x += 1
    if(s[i] == 'y'):
        y += 1
    if(s[i] == 'z'):
        z += 1
    Numx.append(x)
    Numy.append(y)
    Numz.append(z)


Ans = ""
for M in range(m):
    s, e = list(map(int, sys.stdin.readline().split()))
    if(e - s + 1 <= 2):
        Ans += "YES\n"
        continue
    s -= 1
    e -= 1
    x = Numx[e]
    y = Numy[e]
    z = Numz[e]
    if(s != 0):
        x -= Numx[s - 1]
        y -= Numy[s - 1]
        z -= Numz[s - 1]
    if(x == y == z):
        Ans += "YES\n"
        continue
    L = [x, y, z]
    L.sort()
    if(L[0] == L[1] and L[2] == L[1] + 1):
        Ans += "YES\n"
        continue
    if(L[1] == L[2] and L[0] == L[1] - 1):
        Ans += "YES\n"
    else:
        Ans += "NO\n"
sys.stdout.write(Ans)
