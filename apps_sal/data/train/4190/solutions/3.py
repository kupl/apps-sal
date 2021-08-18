vowels = "aeiou"


def is_alt(s):
    if len(s) < 2:
        return False

    prevIsVowel = s[0] in vowels
    for c in s[1::]:
        isVowel = c in vowels

        if prevIsVowel == isVowel:
            return False

        prevIsVowel = isVowel

    return True
