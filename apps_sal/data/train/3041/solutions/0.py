from re import sub


def vowel_start(st):
    return sub('(?<=.)([aeiou])', ' \\1', sub('[^a-z0-9]', '', st.lower()))
