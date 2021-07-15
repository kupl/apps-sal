def isValid(formula):
    s = ''.join(sorted(map(str,formula)))
    return not any(['12' in s,'34' in s,('5' in s)+('6' in s) == 1,('7' in s)+('8' in s) == 0])
