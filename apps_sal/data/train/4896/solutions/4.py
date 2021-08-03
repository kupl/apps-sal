def build_trie(*words):
    return (cheker(words) or {})


def cheker(words, i=1):
    doc, selter = {}, set(e[:i] for e in words if e)
    for fl in selter:
        doc[fl] = cheker(tuple(e for e in words if e[:i] == fl and e != fl), i + 1)
    return None if not words else doc
