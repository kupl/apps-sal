def first_non_repeating_letter(string):
    a = [i for i in string.lower()]
    b = 0
    c = [i for i in string]
    if len(string) == 1:
        return string
    while b < len(a) - 1:
        if a.count(a[b]) == 1:
            return c[b]
        else:
            b += 1
    return ''
