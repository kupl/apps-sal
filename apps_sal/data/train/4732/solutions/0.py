def absent_vowel(x):
    return ['aeiou'.index(i) for i in 'aeiou' if i not in x][0]
