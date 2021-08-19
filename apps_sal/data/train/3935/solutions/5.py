def vowel_recognition(s):
    return sum(((i + 1) * (len(s) - i) for (i, c) in enumerate(s) if c in 'AEIOUaeiou'))
