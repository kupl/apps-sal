for i in range(int(input())):
    x = int(input())
    s = 0
    for i in range(1, x + 1, 2):
        k = x - i + 1
        s += k * k
    print(s)
