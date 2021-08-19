def pick_peaks(a):
    a = [int(i) for i in a]
    pred = 0
    prov = False
    peaks = []
    pos = []
    count = 0
    spusk = True
    for i in range(len(a)):
        if pred == a[i] and spusk == False:
            count += 1
            prov = True
            continue
        if pred > a[i]:
            if prov == True:
                peaks.append(a[i - 1])
                pos.append(i - 1 - count)
            prov = False
            spusk = True
        elif i != 0 and pred < a[i]:
            prov = True
            spusk = False
        pred = a[i]
        count = 0
    d = {'pos': pos, 'peaks': peaks}
    return d
