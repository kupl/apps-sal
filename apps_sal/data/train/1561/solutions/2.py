import sys

t = int(sys.stdin.readline().strip())

while t:
    n = int(sys.stdin.readline().strip())

    if n == 1:
        st = 1
    elif n == 2:
        st = "1 2"
    elif n == 3:
        st = "1 2 3"
    else:

        j = n // 2 + 1
        add = []
        for i in range(n):
            add.append(str(n - i + j - 1))

        st = " ".join(add)
    print(st)

    t -= 1
