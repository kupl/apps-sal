def vowel_start(s):
    r = ''
    for letter in s:
        if letter in 'aeiouAEIOU':
            r += ' ' + letter.lower()
        elif letter.isalnum():
            r += letter.lower()
    return r.lstrip(' ')
