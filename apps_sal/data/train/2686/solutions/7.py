import re
def changer(st):
    st = st.lower().translate(st.maketrans('abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza'))
    return re.sub('[aeiou]',lambda m: m.group().upper(),st)
