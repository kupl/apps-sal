vowels = "aeiou"


def is_alt(s):
    # if string is less than 2 characters, it cannot alternate
    if len(s) < 2:
        return False

    # check if the first character is a vowel or consonant
    prevIsVowel = s[0] in vowels
    for c in s[1::]:
        # check if the next character is a vowel or consonant
        isVowel = c in vowels

        # if the previous character and this character are both vowels
        # or both consanants, return False
        if prevIsVowel == isVowel:
            return False

        # set the previous char state to the current character state
        prevIsVowel = isVowel

    return True
