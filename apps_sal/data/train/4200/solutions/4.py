def is_vowel(c):
    return c in 'aeiouAEIOU'


def vowel_shift(text, n):
    if not text or not n:
        return text
    vowels = [c for c in text if is_vowel(c)]
    n = -n % (len(vowels) or 1)
    vowels = iter(vowels[n:] + vowels[:n])
    return ''.join((c if not is_vowel(c) else next(vowels) for c in text))
