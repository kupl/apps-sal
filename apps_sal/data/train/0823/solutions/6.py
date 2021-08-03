for _ in range(int(input())):
    a = list(map(int, input().split()))
    c = 0
    for i in range(1, 16):
        s = 0
        for j in range(4):
            if i & (1 << j):
                s += a[j]
        if s == 0:
            c = 1
            print("Yes")
            break
    if c == 0:
        print("No")
