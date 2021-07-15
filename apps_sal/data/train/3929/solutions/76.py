def reverse(st):
    st = st.replace('   ',' ')
    st = st.replace('  ',' ')
    st = st.strip()
    return ' '.join(st.split(' ')[::-1])
