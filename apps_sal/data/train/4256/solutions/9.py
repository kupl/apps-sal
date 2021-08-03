import string


def insert_missing_letters(st):
    has_seen = []
    alphabet = string.ascii_lowercase
    retstr = ""
    i = 0
    while i < len(st):
        retstr = retstr + st[i]
        index = alphabet.index(st[i])
        if st[i] not in has_seen:
            while index < len(alphabet):
                if alphabet[index] not in st:
                    retstr = retstr + alphabet[index].upper()
                index = index + 1
        has_seen.append(st[i])
        i = i + 1
    return retstr
