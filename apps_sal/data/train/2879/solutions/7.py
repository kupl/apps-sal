import re


def norm(s):
    s = s.lower()
    s = re.sub('[!\\,;\\:\\?\\.]', '', s)
    s = re.sub('[áàâä]', 'a', s)
    s = re.sub('[éèêë]', 'e', s)
    s = re.sub('[íîï]', 'i', s)
    s = re.sub('[óôö]', 'o', s)
    s = re.sub('[úùûü]', 'u', s)
    return s


def could_be(original, another):
    if not another:
        return False
    another = another.replace(':', ' ')
    s1 = set((norm(w) for w in original.strip().split(' ')))
    s2 = set((norm(w) for w in another.strip().split(' ')))
    return s2 <= s1
