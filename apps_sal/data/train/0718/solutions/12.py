for _ in range(int(input())):
    n = int(input())
    r = 2
    if(n == 1):
        print("0")
        continue
    print("0")
    print("1 1")
    b = 1
    c = 0
    for i in range(3, n + 1):
        for j in range(i):
            print(r, end=" ")
            c = r
            r += b
            b = c
        print()
