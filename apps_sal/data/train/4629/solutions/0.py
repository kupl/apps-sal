def penalty(lst):
    (lst, maxLen) = (list(map(str, lst)), max(map(len, lst)))
    return ''.join(sorted(lst, key=lambda s: s.ljust(maxLen, s[-1])))
