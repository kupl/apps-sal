def get_first(element):
    return element[0]


def sorter(textbooks):
    lst = [(el.lower(), el) for el in textbooks]
    lst1 = sorted(lst, key=get_first)
    return [el[1] for el in lst1]
