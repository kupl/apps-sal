fisHex = f = lambda s: len(s) and (s[0] in 'abcdefABCDEF' and int(s[0], 16)) ^ f(s[1:])
