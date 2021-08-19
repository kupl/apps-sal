def find_lcm(num1, num2):
    if num1 > num2:
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


def crowd(days, x, y, z):
    hrs = days * 24
    abc = find_lcm(x, y)
    abc = find_lcm(abc, z)
    return hrs // abc


t = int(input())
nodays = []
a = []
b = []
c = []
for i in range(t):
    nodays.append(int(input()))
    (d, e, f) = map(int, input().split())
    a.append(d)
    b.append(e)
    c.append(f)
for i in range(t):
    print(crowd(nodays[i], a[i], b[i], c[i]))
