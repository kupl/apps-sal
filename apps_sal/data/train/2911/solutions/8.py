def count_vowels(s=''):
    if not isinstance(s, str):
        return None
    return sum(c in "aeiouAEIOU" for c in s)
