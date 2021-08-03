t = int(input())
for i in range(t):
    A1 = int(input(), 2)
    B1 = int(input(), 2)
    outer = 0
    while(B1 > 0):
        outer += 1
        u = A1 ^ B1
        B1 = (A1 + B1) - u
        A1 = u
    print(outer)
