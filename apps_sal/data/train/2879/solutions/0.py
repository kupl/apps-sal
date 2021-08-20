import re
import unicodedata
NAME = re.compile('[\\w-]+')


def decompose(name):
    standarized = unicodedata.normalize('NFKD', name.lower()).encode('ascii', 'ignore') if type(name) != str else name.lower()
    return re.findall(NAME, standarized)


def could_be(original, another):
    if not another.strip():
        return False
    std_original = decompose(original)
    std_another = decompose(another)
    return all((name in std_original for name in std_another))
