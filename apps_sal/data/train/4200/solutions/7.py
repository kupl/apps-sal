import re

def vowel_shift(text, n):
    if not text:
        return text
    vowels = [c for c in text if c in "AEIOUaeiou"]
    if not vowels:
        return text
    vowels = iter(vowels[-n % len(vowels):] + vowels)
    return re.sub('[AEIOUaeiou]', lambda m: next(vowels), text)
