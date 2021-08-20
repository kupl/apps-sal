n = int(input())
st = str(input())
count = 0
while len(st) > 0:
    h = 0
    if 'RR' in st:
        i = st.index('RR')
        st = st[:i] + st[i + 1:]
        count += 1
        h = 1
    if 'GG' in st:
        i = st.index('GG')
        st = st[:i] + st[i + 1:]
        h = 1
        count += 1
    if 'BB' in st:
        i = st.index('BB')
        st = st[:i] + st[i + 1:]
        h = 1
        count += 1
    if h == 0:
        break
print(count)
