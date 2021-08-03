def solve(s):
    lst_s = list(s)
    i, j = 0, len(s) - 1
    while j > i:
        if lst_s[i] == ' ' or lst_s[j] == ' ':
            if lst_s[i] == ' ':
                i += 1
            if lst_s[j] == ' ':
                j -= 1
            continue
        else:
            lst_s[i], lst_s[j] = lst_s[j], lst_s[i]
            i += 1
            j -= 1
    return ''.join(lst_s)
