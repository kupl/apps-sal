def hop_across(lst):
    def steps(l):
        i, c = 0, 0
        while i < len(l):
            c += 1
            i += l[i]
        return c
    return steps(lst) + steps(lst[::-1])
