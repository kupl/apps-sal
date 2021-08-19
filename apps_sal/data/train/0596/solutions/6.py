# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        if(x == 0):
            print(((y - 1) * y) % 1000000007)
        else:
            inc = y % 2
            if(inc == 0):
                cir = (y - 2) // 2
                a = (x + cir) * (x + cir + 1) + x
                print(a % 1000000007)
            else:
                cir = y // 2
                a = (x + cir - 1) * (x + cir)
                a = (a + x + 2 * cir)
                print(a % 1000000007)
except:
    pass
