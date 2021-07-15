def filter_list(l):
    output = []
    for x in l:
        if type(x) == int:
            output.append(x)
    return output
