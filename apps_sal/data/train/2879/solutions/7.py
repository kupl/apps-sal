import re


def norm(s):
    s = s.lower()
    s = re.sub(r'[!\,;\:\?\.]', '', s)
    s = re.sub(r'[áàâä]', 'a', s)
    s = re.sub(r'[éèêë]', 'e', s)
    s = re.sub(r'[íîï]', 'i', s)
    s = re.sub(r'[óôö]', 'o', s)
    s = re.sub(r'[úùûü]', 'u', s)
    return s


def could_be(original, another):
    if not another:
        return False
    another = another.replace(':', ' ')
    s1 = set(norm(w) for w in original.strip().split(' '))
    s2 = set(norm(w) for w in another.strip().split(' '))
    return s2 <= s1
