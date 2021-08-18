for _ in range(int(input())):
    x, y, k, n = list(map(int, input().split()))
    a = abs(x - y) / 2
    if abs(x - y) % 2 == 0:
        if a % k == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
