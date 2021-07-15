import re
def reverse(st):
    strs = st.strip()
    strss = re.sub(' +', ' ', strs)
    return ' '.join(strss.split(' ')[::-1])

