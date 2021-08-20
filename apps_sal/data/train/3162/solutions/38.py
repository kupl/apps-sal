import re


def compare(s1, s2):
    if s1 and s2 and re.search('[a-zA-Z]', s1) and re.search('[a-zA-Z]', s2):
        return sum((ord(i) for i in str(s1.upper()) if re.search('[a-zA-Z]', i))) == sum((ord(i) for i in str(s2.upper()) if re.search('[a-zA-Z]', i)))
    return True
