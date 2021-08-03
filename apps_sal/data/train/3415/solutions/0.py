def build_palindrome(strng):
    n = 0
    while strng[n:] != strng[n:][::-1]:
        n += 1
    return strng + strng[:n][::-1]
