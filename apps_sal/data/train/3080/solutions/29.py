def who_is_paying(n):
    return [n, n[:2]][:2 - (len(n) < 3)]
