def int_root3(x):
    x3 = int(x**(1 / 3))
    while (x3 + 1)**3 < x:
        x3 += 1
    return x3


def odd_dig_cubic(a, b):
    if 0 <= a <= b:
        left = (int_root3(a) + 1) | 1
        right = int_root3(b) | 1
    elif a <= 0 <= b:
        left = 1
        right = int_root3(b) | 1
    else:  # a<=b<=0
        left = (int_root3(abs(b)) + 1) | 1
        right = int_root3(abs(a)) | 1
    result = []
    for i in range(left, right + 1, 2):
        i3 = i**3
        if set(str(i3)) <= set('13579'):
            if a <= i3 <= b:
                result.append(i3)
            if a <= -i3 <= b:
                result.append(-i3)
    return sorted(result)
