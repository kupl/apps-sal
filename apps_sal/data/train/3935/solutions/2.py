def vowel_recognition(s):
    a = [0] * (len(s) + 1)
    for i, c in enumerate(s.lower()):
        a[i] = (c in 'aeiou') * (i+1) + 2 * a[i-1] - a[i-2]
    return a[-2]

