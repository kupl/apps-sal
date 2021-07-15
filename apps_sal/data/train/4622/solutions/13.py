def double_check(strng):
    return bool(sum([strng.lower()[i-1] == strng.lower()[i] for i in range(1,len(strng))]))
