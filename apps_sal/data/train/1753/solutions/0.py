def least_bribes(bribes):
    mem = {}

    def s(n1, n2):
        if n1 >= n2:
            return 0
        if (n1, n2) in mem:
            return mem[n1, n2]
        r = min((bribes[i] + max(s(n1, i), s(i + 1, n2)) for i in range(n1, n2)))
        mem[n1, n2] = r
        return r
    return s(0, len(bribes))
