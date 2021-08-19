def who_is_paying(n):
    return [n] + ([n[:2]] if len(n) > 2 else [])
