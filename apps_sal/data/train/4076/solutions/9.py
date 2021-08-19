def get_count(words=''):
    if not isinstance(words, str):
        words = ''
    words = words.lower()
    return {'vowels': sum((c in 'aeiou' for c in words)), 'consonants': sum((c.isalpha() and c not in 'aeiou' for c in words))}
