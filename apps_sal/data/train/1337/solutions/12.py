def op_lcm(nm1, nm2):
    if nm1 > nm2:
        nm = nm1
        den = nm2
    else:
        nm = nm2
        den = nm1
    rem = nm % den
    while rem != 0:
        nm = den
        den = rem
        rem = nm % den
    gcd = den
    lcm = int(int(nm1 * nm2) / int(gcd))
    return lcm


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    l = list(map(int, input().split()))
    r = int(input())
    nm1 = l[0]
    nm2 = l[1]
    lcm = op_lcm(nm1, nm2)
    for i in range(2, len(l)):
        lcm = op_lcm(lcm, l[i])
    print(lcm + r)
