def peak_height(mountain):
    M = {(r, c) for (r, l) in enumerate(mountain) for c in range(len(l)) if l[c] == '^'}
    h = 0
    while M:
        M -= {(r, c) for (r, c) in M if {(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)} - M}
        h += 1
    return h
