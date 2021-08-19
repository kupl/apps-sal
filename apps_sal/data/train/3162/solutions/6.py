def stringCount(str):
    try:
        if str.isalpha():
            return sum((ord(alpha) for alpha in str.upper()))
    except AttributeError:
        pass
    return 0


def compare(s1, s2):
    return stringCount(s1) == stringCount(s2)
