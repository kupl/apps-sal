def compare(s1, s2):
    return len(set((sum(map(ord, x.upper() if x and x.isalpha() else '')) for x in [s1, s2]))) == 1
