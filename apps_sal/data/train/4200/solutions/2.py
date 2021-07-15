import re
def vowel_shift(text,n):
    if not text: return text
    vowels = [v for v in text if v in 'aeiouAEIOU']
    n = n % len(vowels) if len(vowels) else n
    shifted_vowels = vowels[-n:] + vowels[:-n]
    return re.sub('[aeiouAEIOU]', lambda _: shifted_vowels.pop(0), text)
