def diff(a, b):
    first = []
    second = []
    for element in a:
        if element not in b:
            first.append(element)
    for word in b:
        if word not in a:
            second.append(word)
    third = first + second
    third = sorted(third)
    for element in third:
        if third.count(element) > 1:
            third.remove(element)
    return third
