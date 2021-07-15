def seven_ate9(str_):
    vals = list(str_)
    deletes = []
    
    for idx, val in enumerate(vals[1:-1], 1):
        if val == '9' \
        and vals[idx - 1] == '7' \
        and vals[idx + 1] == '7':
            deletes.append(idx)
            
    for value in reversed(deletes):
        del vals[value]
            
    return ''.join(vals)
