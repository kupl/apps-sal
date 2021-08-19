t = eval(input())
for g in range(t):
    n = int(input())
    if n == 0:
        print(0)
    elif n == 1:
        print('INFINITY')
    else:
        a = 0
        for x in range(2, n):
            k = 1
            while n >= x ** k:
                k += 1
            k -= 1
            if 2 * x ** k > n:
                a += 1
        print(a + 1)
