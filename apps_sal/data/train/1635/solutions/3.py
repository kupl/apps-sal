def middle_permutation(s):
    s = ''.join(sorted(s, reverse=True))
    return s[ len(s)//2 : (len(s)+3)//2 ] + s[ :len(s)//2 ] + s[ (len(s)+3)//2: ]
