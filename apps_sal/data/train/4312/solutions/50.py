def pick_peaks(a):
    pos = []
    try:
        for k in range(1, len(a) - 1):
            if a[k] > a[k - 1] and a[k] > a[k + 1]:
                pos.append(k)
            elif a[k] > a[k - 1] and a[k] == a[k + 1]:
                i = k + 2
                while i < len(a) - 1 and a[i] == a[k]:
                    i += 1
                
                if a[i] < a[k]:
                    pos.append(k)
                else:
                    k = i
                    
        peaks = [a[i] for i in pos]
        return {'pos': pos, 'peaks': peaks}
    except IndexError:
        print(a)
        print('i=', i)
