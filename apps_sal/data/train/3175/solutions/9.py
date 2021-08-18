import re


def triple_double(num1, num2):
    r3 = re.compile(r'(\d)\1\1')
    f = r3.findall(str(num1))
    if len(f) > 0:
        r2 = re.compile(f[0] + '{2}')
        if len(r2.findall(str(num2))):
            return 1
    return 0
