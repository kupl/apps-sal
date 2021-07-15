import re
def reverse(st):
    st = re.sub(' +', ' ',st)
    st = st.split(" ")
    return (" ".join(st[::-1])).strip()
