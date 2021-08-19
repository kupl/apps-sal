import re


def reverse(st):
    st = re.sub('\\s+', ' ', st)
    return ' '.join(st.split(' ')[::-1]).strip()
