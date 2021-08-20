itr = int(input())
for i in range(itr):
    n = int(input())
    j = int(n / 2) + 1
    while j > 0:
        if j * (j + 1) / 2 <= n:
            print(j)
            break
        j -= 1
