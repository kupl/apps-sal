def powerset(s):
    if not s:
        return [[]]
    result = powerset(s[1:])
    return result + [[s[0]] + subset for subset in result]
