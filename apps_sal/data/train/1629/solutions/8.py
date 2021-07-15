def exchange_sort(sequence):
    a=sequence[:]
    seven=a.count(7)
    eight=a.count(8)
    r=0
    for i in range(seven,len(a)):
        if a[i]==7:
            r+=1
            if i<seven+eight and 8 in a[:seven]:
                j=a.index(8)
            else:              
                for j in range(seven):
                    if a[j]!=7:
                        break
            a[i],a[j]=a[j],a[i]
    r+=a[seven+eight:].count(8)
    return r
