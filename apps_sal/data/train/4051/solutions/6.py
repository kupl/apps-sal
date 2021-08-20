def toUnderScore(s):
    return ''.join(('_' + x if (x.isupper() or x.isnumeric()) and (not (x.isnumeric() and s[i - 1].isnumeric())) and (s[i - 1] != '_') and (i != 0) else x for (i, x) in enumerate(s)))
