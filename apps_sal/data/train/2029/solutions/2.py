import sys

n = int(sys.stdin.readline().strip())
if n % 2 == 0:
    print("NO")
else:
    print("YES")
    x = []
    y = []
    for i in range(1, 2 * n + 1):
        if i % 4 == 1 or i % 4 == 0:
            x.append(i)
        else:
            y.append(i)
    print(" ".join(list(map(str, x))) + " " + " ".join(list(map(str, y))))
