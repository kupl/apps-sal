n = int(input())
l = n * 2 - 1
for i in range(l):
    for j in range(l):
        mins = min(i, j)
        if mins >= l - i:
            mins = l - i - 1
        mins = min(mins, l - j - 1)
        print(n - mins, end= " ")
    print()

