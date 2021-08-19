def tops(msg):
    (i, l, step, st) = (2, 2, 2, [])
    while l < len(msg):
        st.insert(0, msg[l:l + i])
        step += 3
        l += step + i
        i += 1
    return ''.join(st)
