def find_missing_number(s):
    l = s.split(' ')
    if s == '':
        return 0
    st = []
    for x in l:
        for c in l:
            if c.isalpha():
                st.append(c)
        if len(st) > 0:
            return 1
        elif sorted([x for x in l]) == [str(y) for y in range(1,len(l)+1)]:
            return 0
        elif sorted([x for x in l]) != [str(y) for y in range(1,len(l)+1)]:
            missing = []
            for a in range(1,len(l)+1):
                if str(a) not in [x for x in l]:
                    missing.append(int(a))
                    return min(missing)
