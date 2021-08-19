def recoverSecret(a):
    out = list(zip(*a))  # transpose the list
    h = [j for j in (set(out[0]) - set(out[1] + out[2]))]  # find the first letter
    for i in a:
        if i[0] in h:  # find triplets starting with that letter
            i[:2], i[2] = i[1:], ''   # remove the first letter and move other letters up

    return h[0] + recoverSecret(a) if h else str()  # return the first letter plus the recursion on the rest
