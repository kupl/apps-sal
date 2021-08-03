def find_children(dancing_brigade):
    a = sorted(dancing_brigade)
    b = ''
    for i in range(len(a)):
        b += a[i]
        for j in range(i + 1, len(a)):
            if a[i].lower() == a[j].lower():
                b += a[j]
    return b[:len(a)]
