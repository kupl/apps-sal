def count_adjacent_pairs(st):
    st = st.lower().split()
    check, ret, k = None, 0, 0
    for e in st:
        if e == check and k:
            continue
        if e == check and not k:
            ret, k = ret + 1, 1
        else:
            check, k = e, 0
    return ret
