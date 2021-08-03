def sorter(textbooks):
    r = {i.lower(): i for i in textbooks}
    return [r[i] for i in sorted(r)]
