def solve(s):
    vowels = sorted([ch for ch in s if ch in 'aeiou'])
    consonants = sorted([ch for ch in s if ch not in 'aeiou'])
    
    if abs(len(vowels) - len(consonants)) > 1:
        return 'failed'
    
    ret = ''
    
    if len(vowels) == len(consonants):
        for v, c in zip(vowels, consonants):
            ret += f'{v}{c}'
    else:
        if len(consonants) > len(vowels):
            zipped = zip(consonants, vowels)
            last = consonants[-1]
        else:
            zipped = zip(vowels, consonants)
            last = vowels[-1]
            
        for c, v in zipped:
            ret += f'{c}{v}'
        ret += last
    return ret 
