def kontti(st):
    r = []
    for s in st.split():
        a,s = '',list(s)
        if not any(i in s for i in 'aeiouyAEIOUY'):
            r.append(''.join(s))
        else:
            while s:
                a += s.pop(0)
                if a[-1] in 'aeiouyAEIOUY':
                    break
            r.append(f"ko{''.join(s)}-{a}ntti")
    return ' '.join(r)
