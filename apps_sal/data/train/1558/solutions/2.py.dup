t = int(input(''))
for v in range(t):
    a = input('').split(' ')
    n = int(a[0])
    m = int(a[1])
    ans = [0] * (n * m)
    for k in range(0, n * m, 1):
        su = 2 * ((n * m - 1) // (k + 1) + 1)
        g = 0
        while(g < n * m):
            j = g % (m)
            i = g // m
            #print((j*n + i),g,k+1)
            if((j * n + i) % (k + 1) == 0):
                su = su - 1
            # print(g,su)
            g = g + (k + 1)
        print(su, end=' ')
    print('')
