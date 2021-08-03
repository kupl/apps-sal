t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i >= j:
                print(int((i + 1) * (i + 2) / 2) - j, end='')
        print()
