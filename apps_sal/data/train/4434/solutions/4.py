def first_non_repeated(s):
    print(s)
    return next((i for i in s if s.count(i) == 1), None)
