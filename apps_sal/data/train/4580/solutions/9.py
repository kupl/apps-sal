def tiaosheng(failed_counter):
    a = [1]*200
    j = 0
    for i in failed_counter:
        i += 3 * j
        j += 1
        a.insert(i+1,0)
        a.insert(i+1,0)
        a.insert(i+1,0)
    return sum(a[1:61])
