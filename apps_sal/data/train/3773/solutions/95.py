def isValid(f):
    y = ''.join(map(str, sorted(f)))
    return '12' not in y and '34' not in y and ('56' in y or ('5' not in y and '6' not in y)) and ('7' in y or '8' in y)
