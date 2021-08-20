def spoonerize(words):
    x = words.split()
    (first, second) = (list(x[0]), list(x[1]))
    (first[0], second[0]) = (second[0], first[0])
    str_list = ''.join(first) + ' ' + ''.join(second)
    return str_list
