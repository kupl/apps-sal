t = int(input())
for i in range(t):
    n = int(input())

    def compute_hcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    if(n == 1):
        print(1, end=" ")
        print(1)
    elif(n > 1):
        a = 0
        b = 10**n
        if(n % 2 == 0):
            a += 10**(n // 2)
        elif(n % 2 != 0):
            a += 10**((n // 2) + 1)
        hcf = 0
        hcf = compute_hcf(a, b)
        a1 = 0
        b1 = 0
        a1 = a // hcf
        b1 = b // hcf
        print(a1, end=" ")
        print(b1)
