def find_children(dancing_brigade):
    c = ''
    L = sorted(dancing_brigade.lower())
    for i in range(len(L)):
        if L[i] != c:
            L[i] = L[i].upper()
            c = L[i].lower()
    return ''.join(L)
