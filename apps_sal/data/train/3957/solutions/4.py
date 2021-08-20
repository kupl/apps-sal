def uniq_c(l):
    return (lambda x: [(x[i][1], x[i][0] - x[i - 1][0]) if i > 0 else (x[0][1], x[0][0] + 1) for i in range(len(x))])((lambda t: [(t[i][0], t[i][1]) for i in range(len(t) - 1) if t[i][1] != t[i + 1][1]])(list(enumerate(l))) + [(len(l) - 1, l[-1])]) if l != [] else []
