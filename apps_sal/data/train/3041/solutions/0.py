from re import sub
def vowel_start(st):
    return sub(r'(?<=.)([aeiou])', r' \1', sub(r'[^a-z0-9]', '', st.lower()))

