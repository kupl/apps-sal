def compare(s1, s2):
    if s1 is None or not s1.isalpha():
        s1 = ''
    if s2 is None or not s2.isalpha():
        s2 = ''
    return sum(ord(letter) for letter in s1.upper()) == sum(ord(letter) for letter in s2.upper())
