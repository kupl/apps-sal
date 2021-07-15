def bubblesort_once(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l = l[:i] + [ l[i+1] ] + [ l[i] ] + l[i+2::]
    return l
