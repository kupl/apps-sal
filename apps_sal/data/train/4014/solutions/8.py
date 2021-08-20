def combine_strings(*args):
    sol = ''
    words = []
    if len(args) == 0:
        return sol
    for a in args:
        words.append(list(a))
    while 1:
        for (i, w) in enumerate(words):
            if len(w) != 0:
                sol = sol + w[0]
                words[i].remove(w[0])
        if all((not element for element in words)):
            break
    return sol
