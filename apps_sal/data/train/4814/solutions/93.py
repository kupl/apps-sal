def inversa(s):
    large = 0
    sInversa = ""
    index = -1
    sLittle = ""
    for quantity in s:
        large += 1
    while large >= 1:
        sInversa += s[index]
        index -= 1
        large -= 1
    for letters in sInversa:
        if 65 <= ord(letters) <= 90:
            sLittle += chr(ord(letters) + 32)
        else:
            sLittle += letters
    return sLittle


def is_palindrome(s):
    sPalindrome = ""
    compare = inversa(s)
    for lettersPalindrome in s:
        if 65 <= ord(lettersPalindrome) <= 90:
            sPalindrome += chr(ord(lettersPalindrome) + 32)
        else:
            sPalindrome += lettersPalindrome
    return compare == sPalindrome
