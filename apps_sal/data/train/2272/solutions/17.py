from numpy import *
(a, b) = loadtxt(open((c := 0)), 'i', skiprows=1)
l = 1 << 29
while l:
    u = l
    l >>= 1
    c += sum(diff(searchsorted(sort(r_[b % u - u, b % u]), ([u], [l]) - a % u).T)) % 2 * l
print(c)
