def fun(n):
    b = bin(n - 1).replace("0b", "")
    if b.count("0") == 0:
        return n
    l = len(b)
    s = "1" * l
    return (int(s, 2) + 1)


for i in range(int(input())):
    n = int(input())
    print(fun(n))
