def solve(s):
    vowels = sorted([x for x in s if x in ("aeiou")])
    consonants = sorted([x for x in s if x not in vowels])
    difference = len(vowels) - len(consonants)
    s = ""
    if abs(difference) >= 2:
        return "failed"
    elif abs(difference) == 1:
        if difference == 1:
            s += vowels.pop(0)
        else:
            s += consonants.pop(0)
    if s == "" or s[0] not in "aeiou":
        s += ''.join(''.join(pair) for pair in zip(vowels, consonants))
    else:
        s += ''.join(''.join(pair) for pair in zip(consonants, vowels))
    return s
