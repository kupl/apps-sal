def count_vowels(s=''):
    return len([c for c in s.lower() if c in 'aeiou']) if isinstance(s, str) else None
