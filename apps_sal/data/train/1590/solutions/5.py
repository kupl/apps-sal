for a0 in range(int(input())):
    x = list(map(int, input().split()))
    x.sort()
    if x[0] + x[1] >= x[2] - 1:
        print("Yes")
    else:
        print("No")
