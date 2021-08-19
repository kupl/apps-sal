P = print
R = range
n = int(input())
x = ' '.join([' '.join((str(j ** i) for i in R(1, 11) if j ** i <= n)) for j in R(2, n + 1) if 0 == sum((j % i == 0 for i in R(2, j)))])
P(len(x.split()))
P(x)
