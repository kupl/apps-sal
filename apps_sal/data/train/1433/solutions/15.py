import sys


def analyze(string):
    sevens = 0
    low = 0
    mid = 0
    high = 0
    fours = 0
    for c in string:
        if c > '7':
            high = high + 1
        elif c == '7':
            sevens = sevens + 1
        elif c == '4':
            fours = fours + 1
        elif c < '4':
            low = low + 1
        else:
            mid = mid + 1

    return (sevens, fours, high, mid, low)


def solve(A, B):
    l = len(A)
    a = analyze(A)
    b = analyze(B)
    (a_s, a_f, a_h, a_m, a_l) = a
    (b_s, b_f, b_h, b_m, b_l) = b

    c_s = 0
    c_f = 0

    if a_h > b_h:
        l = l - (a_h)
        b_m = max(b_m - (a_h - b_h), 0)
    elif b_h > a_h:
        l = l - (b_h)
        a_m = max(a_m - (b_h - a_h), 0)
    else:
        l = l - a_h

    c_s = a_s + b_s

    l = l - c_s

    if l <= 0:
        c_s = c_s + l
        return (c_s, c_f)

    a_m = max(a_m - b_s, 0)
    b_m = max(b_m - a_s, 0)

    l = l - max(a_m, b_m)

    c_f = a_f + b_f
    l = l - c_f

    if l <= 0:
        c_f = c_f + l

    return (c_s, c_f)


def show(s, f):
    print(s * '7' + f * '4')


f = sys.stdin

for test in range(int(f.readline())):
    A = f.readline().rstrip()
    B = f.readline().rstrip()
    (c_s, c_f) = solve(A, B)
    show(c_s, c_f)
