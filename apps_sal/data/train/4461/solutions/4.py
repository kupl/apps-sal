def boxes_packing(length, width, height):

    def incr(s):
        return all((x < y for (x, y) in zip(s, s[1:])))
    return all((incr(s) for s in zip(*sorted((sorted(b) for b in zip(length, width, height))))))
