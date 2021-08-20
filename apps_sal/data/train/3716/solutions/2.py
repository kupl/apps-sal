import string


def unusual_sort(array):
    upper = sorted([i for i in array if i in list(string.ascii_uppercase)])
    lower = sorted([it for it in array if it in list(string.ascii_lowercase)])
    intint = sorted([num for num in array if num in list(map(int, list(string.digits)))])
    strints = sorted([e for e in array if e in list(string.digits)])
    upper.extend(lower)
    intint.extend(strints)
    want = []
    for i in intint:
        if type(i) is not int:
            want.append((int(i), i))
        else:
            want.append((i, i))
    ans = [i[1] for i in sorted(want, key=lambda x: x[0])]
    upper.extend(ans)
    return upper
