import string


def insert_missing_letters(st):
    tbl = dict.fromkeys(map(ord, st.upper()))
    result = []
    seen = set()
    for c in st:
        if c not in seen:
            seen.add(c)
            c += string.ascii_uppercase[string.ascii_lowercase.find(c) + 1:].translate(tbl)
        result.append(c)
    return ''.join(result)
