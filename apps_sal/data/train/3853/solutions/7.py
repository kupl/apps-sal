def numeric_formatter(t, s='1234567890'):
    (idx, arr_t) = (0, list(t))
    for i in range(len(arr_t)):
        if arr_t[i].isalpha():
            arr_t[i] = s[idx % len(s)]
            idx += 1
    return ''.join(arr_t)
