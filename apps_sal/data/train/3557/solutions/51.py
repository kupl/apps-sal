def odd_count(n):
    return n // 2
    oddlist = []
    for eachnumber in range(n-1,0,-1):
        if eachnumber % 2 == 0:
            continue
        else:
            oddlist.append(eachnumber)
    return len(oddlist)
