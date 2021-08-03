def get_count(words=None):
    result = {'vowels': 0, 'consonants': 0}
    vowels, consonants = 'aeiou', 'bcdfghjklmnpqrstvwxyz'

    if type(words) == str:
        result['vowels'] = len([v for v in words.lower() if v in vowels])
        result['consonants'] = len([c for c in words.lower() if c in consonants])

    return result
