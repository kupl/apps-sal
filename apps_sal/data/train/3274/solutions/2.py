def solve(s): return len(__import__('re').match(r'^(.*).*\1$', s).group(1))
