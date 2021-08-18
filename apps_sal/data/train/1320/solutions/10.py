t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1 or n == 2:
        print("B")
        continue
    if n == 3:
        print("A")
        continue

    if n > 3:
        if n - 3 > 0:
            print("B")
        else:
            print("A")
