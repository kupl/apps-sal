def vowel_recognition(s):
    return sum((len(s) - i) * (i + 1) for i, ch in enumerate(s) if ch in 'aeiouAEIOU')
