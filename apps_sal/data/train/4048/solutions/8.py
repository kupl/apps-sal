def pig_latin(w): return len(w) < 4 and w or "%s%say" % (w[1:], w[0])
