n = int(input())
for i in range(n):
    x = int(input())
    f = 1
    j = 1
    while j <= x:
        f *= j
        j += 1
    print(f)
