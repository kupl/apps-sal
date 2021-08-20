def is_substitution_cipher(s1, s2):
    translation = {}
    back_translation = {}
    for (ch1, ch2) in zip(s1, s2):
        if ch1 in translation:
            if not translation[ch1] == ch2:
                return False
        else:
            translation[ch1] = ch2
        if ch2 in back_translation:
            if not back_translation[ch2] == ch1:
                return False
        else:
            back_translation[ch2] = ch1
    return True
