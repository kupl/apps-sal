f = []
for i in range(100000 + 1):
    if i == 0:
        f.append(0)
    elif i == 1:
        f.append(1)
    else:
        f.append(f[-1] + f[-2])

for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        for j in range(i):
            print(f[count], end=" ")
            count += 1
        print()
