def compare(s1, s2):
    return (sum(ord(i.upper()) for i in s1) if type(s1) == str and s1.isalpha() else 1) == (sum(ord(i.upper()) for i in s2) if type(s2) == str and s2.isalpha() else 1)
