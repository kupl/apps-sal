def keep_order(ary, val):
    idx = 0
    for i in range(len(ary)):
        if val > ary[idx]:
            idx += 1
        else:
            return idx
    return idx
