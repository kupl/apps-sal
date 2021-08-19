def sort(d):
    if d == 0:
        return 1
    if d == 1:
        return 2
    if d == 2:
        return 3


def sort1(s, e):
    if s < e:
        p = s * e
    return p


def function1(a):
    if a == 0:
        return
    for b in function1(a // 5):
        yield b
    c = a % 5
    yield c


def function(m):
    return int(''.join((str(2 * c) for c in function1(m))) or '0')


t = eval(input())
while t > 0:
    n = eval(input())
    a = 0
    m = 1
    p = 0
    q = 0
    r = 0
    if m == 1:
        p = 1
        m = m + 1
    if m == 2:
        q = 1
        m = m + 1
    if m == 3:
        r = 1
        m = m + 1
    if n == 1:
        print(a)
    else:
        print(function(n - 1))
    t = t - 1
ml = [1, 5, 7, 9]
s = 0
p = ml[s]
l = r + 1
r = e = 0
d = False
te = ml[s]
ml[s] = ml[r]
ml[r] = te
