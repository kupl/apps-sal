def sorter(textbooks):
    lst = sorted([(el.lower(), el) for el in textbooks])
    return [el[1] for el in lst]
