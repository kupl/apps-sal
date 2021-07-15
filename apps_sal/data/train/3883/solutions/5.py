import re
def solve(s):
    vowels = sorted(re.findall(r'[aeiou]', s))[::-1]
    consonant = sorted(re.findall(r'[^aeiou]', s))[::-1]
    if abs(len(consonant) - len(vowels)) > 1: return 'failed'

    out = []
    if len(vowels) >= len(consonant):
        while vowels and consonant:
            out.append(vowels.pop())
            out.append(consonant.pop())
    
    else:
        while vowels and consonant:
            out.append(consonant.pop())
            out.append(vowels.pop())

    return consonant and ''.join(out + consonant) or ''.join(out + vowels)
