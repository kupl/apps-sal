def spacey(a):
    return list(__import__('itertools').accumulate(a))
