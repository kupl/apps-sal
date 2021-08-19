from numpy import *
(a, b) = loadtxt(open(0), 'i', skiprows=1)
c = 0
l = 1 << 29
while l:
    u = l
    l >>= 1
    c += sum(diff(searchsorted(sort(hstack((b % u - u, b % u))), ([u], [l]) - a % u).T)) % 2 * l
print(c)
