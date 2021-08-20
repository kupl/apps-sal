def err_bob(s):
    res = ''
    for (i, c) in enumerate(s):
        res += c
        if i == len(s) - 1 or s[i + 1] in ' .,:;!?':
            if c.islower() and c not in 'aeiou':
                res += 'err'
            if c.isupper() and c not in 'AEIOU':
                res += 'ERR'
    return res
