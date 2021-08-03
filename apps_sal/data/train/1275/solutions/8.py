def maximum(a, b):
    if a > b:
        return a
    else:
        return b


for _ in range(int(input())):
    n, m = input().split()
    arr = [0] * int(n)
    val = input().split()
    maxi = 0
    mini = int(n) + 1
    for j in val:
        if int(j) > maxi:
            maxi = int(j)
        if int(j) < mini:
            mini = int(j)
    for i in range(int(n)):
        print(maximum(abs(i - mini), abs(maxi - i)), end=" ")
    print()
