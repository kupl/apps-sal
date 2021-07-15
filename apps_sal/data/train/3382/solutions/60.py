def lowercase_count(strng):
    return sum([1 if c.islower() else 0 for c in strng])
