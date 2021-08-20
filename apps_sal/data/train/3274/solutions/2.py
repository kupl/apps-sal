def solve(s):
    return len(__import__('re').match('^(.*).*\\1$', s).group(1))
