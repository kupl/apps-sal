def sorter(textbooks):
    d = {t.lower(): t for t in textbooks}
    return [d[t] for t in sorted(d)]
