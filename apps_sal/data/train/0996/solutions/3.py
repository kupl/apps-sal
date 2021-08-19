# cook your dish here
try:
    n1 = int(input())
    wina = winb = ma = mb = n = m = 0
    for i in range(n1):
        a, b = list(map(int, input().split()))
        n += a
        m += b
        if n > m and n - m > ma:
            ma = n - m
        elif n < m and m - n > mb:
            mb = m - n
    if ma > mb:
        print('1', ma)
    elif ma < mb:
        print('2', mb)
except:
    pass
