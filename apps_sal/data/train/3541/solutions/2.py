def find_page_number(p):
    r, i = [], 0

    while i < len(p):
        if p[i] != i + 1:
            r += [p.pop(i)]
            i -= 1
        i += 1

    return r
