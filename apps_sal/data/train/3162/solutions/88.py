def compare(s1,s2):
    if s1 is None or any(not char.isalpha() for char in s1):
        s1 = ""
    if s2 is None or any(not char.isalpha() for char in s2):
        s2 = ""
    return sum(ord(char) for char in s1.upper()) == sum(ord(char) for char in s2.upper())
