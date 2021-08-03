def word_pattern(pattern, string):
    print((pattern, string))
    string = string.split(' ')
    m = len(string)
    x = {}
    if m != len(pattern) or len(set(pattern)) != len(set(string)):
        return False
    for k, s in zip(pattern, string):
        if k in x and s != x[k]:
            return False
        x[k] = s
    return True
