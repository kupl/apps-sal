def clean(s):
    if s == None:
        return ''
    elif s.isalpha():
        return s.upper()
    else:
        return ''


def compare(s1, s2):
    (s1, s2) = (clean(s1), clean(s2))
    sum1 = sum((ord(letter) for letter in s1))
    sum2 = sum((ord(letter) for letter in s2))
    return sum1 == sum2
