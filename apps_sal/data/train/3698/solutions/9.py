import re


def ironyarder(m):
    lst = []
    if m[0].isupper():
        lst.append('Iron')
    if m[0].lower() in 'aeiou':
        lst.append('Yard')
    return ' '.join(lst)


def tiy_fizz_buzz(s):
    return re.sub(r'[A-Zaeiou]', ironyarder, s)
