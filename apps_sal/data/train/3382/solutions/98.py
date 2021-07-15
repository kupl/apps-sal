def lowercase_count(strng):
    return len([i for i in strng if i.lower() == i and i.isalpha()])
