for _ in range(int(input())):
    n = int(input())
    if(n == 1):
        print("1")
        continue
    print("1")
    r = 2
    for i in range(n - 2):
        t = str(r)
        t += " " * i
        r += 1
        t += str(r)
        r += 1
        print(t)
    for i in range(n):
        print(r, end="")
        r += 1
    print()
