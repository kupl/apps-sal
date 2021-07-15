def keep_order(ary, val):
    if not ary:
        return 0
    for x in range(len(ary)):
        if val <= ary[x]:
            return x
    return x+1        
    

