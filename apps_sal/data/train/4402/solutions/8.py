def solve(st):
    new_st = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in st:
        new_st.append(letters.index(i))
    new_st = sorted(new_st)
    
    a = [(new_st[i+1] - new_st[i]) for i in range(len(new_st)-1)]
    if a.count(1) == len(st) - 1:
        return True
    return False
