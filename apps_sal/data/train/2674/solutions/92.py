def two_sort(array):
    k=[]
    k.append(sorted(array)[0])
    j=[]
    for i in k[0]:
        j.append(i)
        
    return '***'.join(j)
