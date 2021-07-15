def capitalize(s,ind):
    c = ""
    for i in range(len(s)):
        k = 0
        for j in range(len(ind)):
            if i == ind[j]:
                c += s[i].upper()
                k += 1
            else:
                continue
        if k == 0:
            c += s[i]
    return c

