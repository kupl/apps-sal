def reverse(st):
    l = st.strip().split()
    if len(l) > 1:
        l = l[::-1]
        return ' '.join(l).strip()
    return ' '.join(l).strip()
