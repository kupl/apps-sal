def pick_peaks(a):
    ind = []
    val = []
    for i in range(1, len(a)-1):
            if  a[i-1] < a[i] and a[i] > a[i+1]:
                ind.append(i)
                val.append(a[i])
            elif a[i] > a[i-1] and a[i] == a[i+1]:
                for j in range(i+1, len(a)-1):
                        if a[j] == a[i] and a[j]<a[j+1]:
                            break
                        elif a[j] == a[i] and a[j+1]<a[j]:
                            ind.append(i)
                            val.append(a[i])
                            break
    return {'pos': ind, 'peaks': val}
