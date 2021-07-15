d = []
s1 = lambda n:1+2**n+3**n
s2 = lambda n:1+2**n+4**n
s3 = lambda n:sum(i**n for i in range(1,7))
st = lambda n:s3(n)-s2(n)-s1(n)
for i in range(1500):
    r = (st(i + 1) - 5 * st(i) - 4) // 4
    if not r % 10 : d.append(r)
find_mult10_SF=lambda n:d[n-1]
