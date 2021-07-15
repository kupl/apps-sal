def bubble(l):
    arr = []
    for j in range(len(l)-1,0,-1):
        for i in range(j):
            if l[i]>l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                arr.append(l[:])
    return arr
