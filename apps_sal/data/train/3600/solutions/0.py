def move_vowels(s):
    return ''.join(sorted(s, key=lambda k: k in 'aeiou'))
