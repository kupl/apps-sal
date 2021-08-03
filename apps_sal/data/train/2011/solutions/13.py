n = int(input())
x = n
z = 0
t = 0
fty = []
for i in range(min(1000, n)):
    z = 0
    x = str(x)
    for j in range(len(x)):
        z += int(x[j])
    x = int(x)
    if (x + z) == n:
        t += 1
        fty += [x]
    x -= 1
fty.sort()
if t == 0:
    print(t)
else:
    print(t)
    for i in fty:
        print(i)
