# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    red = 0
    i = 0
    while red < n:
        if a[i] == 0:
            red += 1
        else:
            break
        i += 1

    i = n - 1
    while red < n:
        if a[i] == 0:
            red += 1
        else:
            break
        i -= 1

    if red < n:
        print(n - red)
    else:
        print("1")
