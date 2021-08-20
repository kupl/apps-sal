def get_count(words=''):
    if not isinstance(words, str):
        return {'vowels': 0, 'consonants': 0}
    letter = ''.join([c.lower() for c in words if c.isalpha()])
    vowel = ''.join([c for c in letter if c in 'aeiou'])
    consonant = ''.join([c for c in letter if c not in 'aeiou'])
    return {'vowels': len(vowel), 'consonants': len(consonant)}
