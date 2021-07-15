def is_haiku(text):
    import string
    vow = 'aeiouy'

    def syl_in_word(word):
        if word is '':
            return 0
        syls = sum([1 for ind, l in enumerate(word[:-1]) if (l in vow) and word[ind + 1] not in vow])
        if word[-1] in vow:
            if word[-1] != 'e' or (len(word)>1 and word[-2] in vow) or syls == 0:
                syls += 1
        return syls

    strings = text.split('\n')
    syls = []
    for s in strings:
        # lower and clear punctuation
        s = ''.join([c for c in s.lower() if c not in string.punctuation])
        syls.append(sum([syl_in_word(word) for word in s.split(' ')]))

    return syls == [5, 7, 5]
