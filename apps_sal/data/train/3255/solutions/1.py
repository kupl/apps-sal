def only_duplicates(string):
    return "".join([x for x in string if string.count(x) > 1])
