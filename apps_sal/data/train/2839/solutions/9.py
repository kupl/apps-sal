def count_adjacent_pairs(st):
    #print(st)
    st = st.lower().split()
    cnt = 0
    on = False
    for i in range(1,len(st)):
        if st[i] == st[i-1]:
            if not on: 
                cnt += 1
                on = True
        else:
            on = False
    return cnt
