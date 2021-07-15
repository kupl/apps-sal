def find_needed_guards(k):
    b = ''.join('1' if g else '0' for g in k)
    return sum(len(ng) // 2 for ng in b.split("1"))
