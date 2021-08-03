import re


def vowel_start(st):
    st = re.sub("[^a-zA-Z0-9]", "", st.lower())
    r = st[0] if len(st) else ""
    for s in st[1:]:
        r += (" " if s in "aeiou" else "") + s
    return r
