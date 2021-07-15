def middle_permutation(s):
    s = ''.join(sorted(s))
    return s[len(s)//2-1:(len(s)+1)//2][::-1] + s[(len(s)+1)//2:][::-1] + s[:len(s)//2-1][::-1]
