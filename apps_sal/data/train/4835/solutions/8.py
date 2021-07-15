import string as st
def okkOokOo(s):
    trans = st.maketrans("Ook","001")
    return ''.join(chr(int(st.translate(i, trans, ", ?!"), base=2)) for i in s.split('? '))
