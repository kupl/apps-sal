"""
##########################################
This File is submitted by SAURABH SISODIA
EMAIL ... ssisodia507@gmail.com

##########################################
"""
for _ in range(int(input())):
    (n, m, x, y) = map(int, input().split())
    k1 = (n - 1) // x
    k2 = (m - 1) // y
    if n == 1 or m == 1:
        if x * k1 == n - 1 and y * k2 == m - 1:
            print('Chefirnemo')
        else:
            print('Pofik')
    elif x * k1 == n - 1 and y * k2 == m - 1:
        print('Chefirnemo')
    else:
        k1 = (n - 2) // x
        k2 = (m - 2) // y
        if x * k1 == n - 2 and y * k2 == m - 2:
            print('Chefirnemo')
        else:
            print('Pofik')
