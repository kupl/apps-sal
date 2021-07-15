is_divisible_by_6=lambda s:[n for n in map(''.join,__import__('itertools').product(*(c=='*'and'0123456789'or c for c in s)))if int(n)%6<1]
