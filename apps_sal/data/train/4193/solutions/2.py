(s, hh) = (-464148, [])
while s < 464159:
    v = s ** 3
    (sv, b) = (str(v), 1)
    for c in sv:
        if not c in '-13579':
            b = 0
            break
    if b:
        hh.append(v)
    s += 1


def odd_dig_cubic(a, b):
    r = []
    for i in hh:
        if i >= a:
            if i <= b:
                r.append(i)
            else:
                break
    return r
