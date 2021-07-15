def get_strings(stra):
    string = stra.lower()
    dc = {}
    for i in string:
        if i == ' ':
            continue
        dc[i] = '*' * string.count(i)
    
    return ','.join([k + ':' + v for k, v in list(dc.items())])

