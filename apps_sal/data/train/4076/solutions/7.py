def get_count(s=''):
    ret = {'vowels': 0, 'consonants': 0}
    if type(s) != str:
        return ret
    for c in s.lower():
        if c in 'aeiou':
            ret['vowels'] += 1
        elif c.isalpha(): # letter but not vowel because elif
            ret['consonants'] += 1
    return ret
