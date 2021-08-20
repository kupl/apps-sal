def vowel_back(s):
    return ''.join((e[e[0] in 'code'] for e in [(chr(ord(x) - max(1, 'co de'.index(x)) if x in 'code' else 97 + (ord(x) - 97 - 5 if x in 'aiu' else ord(x) - 97 + 9) % 26), x) for x in s]))
