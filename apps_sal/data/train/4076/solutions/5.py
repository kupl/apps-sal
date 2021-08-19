is_vowels = set('aeiou').__contains__
is_conson = set('bcdfghjklmnpqrstvwxyz').__contains__


def get_count(words=None):
    result = {'vowels': 0, 'consonants': 0}
    if words and type(words) == str:
        for c in words.lower():
            result['vowels'] += is_vowels(c)
            result['consonants'] += is_conson(c)
    return result
