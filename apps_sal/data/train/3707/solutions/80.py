def sorter(textbooks):
    return [a[1] for a in sorted([(b.lower(), b) for b in textbooks])]
