def change(st):
    s = set(filter(str.isalpha, st.lower()))
    return ''.join(('01'[chr(97 + i) in s] for i in range(26)))
