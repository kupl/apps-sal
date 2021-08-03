def sorter(textbooks):
    ret = [t for t in textbooks]
    ret.sort(key=lambda x: x.lower())
    return ret
