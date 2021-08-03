is_vowel = set("aeiouAEIOU").__contains__


def count_vowels(s=''):
    if type(s) == str:
        return sum(map(is_vowel, s))
