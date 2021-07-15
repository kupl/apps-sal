def count_feelings(s, arr):
    c = 0
    for i in arr:
        r = True
        for j in i:
            if (j not in s) or (i.count(j) > s.count(j)):
                r = False
        if r: c+=1
    return str(c) + ' feelings.' if c != 1 else str(c) + ' feeling.'
