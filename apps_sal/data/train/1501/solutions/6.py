def mirror_down(e, r, l, u, d):
    edge = (2 * e) + d
    right = r * 2
    left = l * 2
    up = u
    down = u
    return [edge, right, left, up, down]


def mirror_up(e, r, l, u, d):
    edge = (2 * e) + u
    right = r * 2
    left = l * 2
    up = d
    down = d
    return [edge, right, left, up, down]


def mirror_left(e, r, l, u, d):
    edge = (2 * e) + l
    right = r
    left = l
    up = u * 2
    down = d * 2
    return [edge, right, left, up, down]


def mirror_right(e, r, l, u, d):
    edge = (2 * e) + r
    right = r
    left = l
    up = u * 2
    down = d * 2
    return [edge, right, left, up, down]


s = input('').split(' ')
n, q = (int(s[0]), int(s[1]))
e = (2**(n + 1)) - 2
l = n + 1
r = n + 1
u = 1
d = 2**n
while(q != 0):
    s = input('').split(' ')
    if(len(s) == 2):
        c = int(s[1])
        if(c == 1):
            a = mirror_right(e, r, l, u, d)
            e = a[0]
            r = a[1]
            l = a[2]
            u = a[3]
            d = a[4]
        if(c == 2):
            a = mirror_left(e, r, l, u, d)
            e = a[0]
            r = a[1]
            l = a[2]
            u = a[3]
            d = a[4]
        if(c == 3):
            a = mirror_up(e, r, l, u, d)
            e = a[0]
            r = a[1]
            l = a[2]
            u = a[3]
            d = a[4]
        if(c == 4):
            a = mirror_down(e, r, l, u, d)
            e = a[0]
            r = a[1]
            l = a[2]
            u = a[3]
            d = a[4]

    else:
        print(e % 1000000007)
    q -= 1
