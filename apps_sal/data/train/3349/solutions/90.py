def find_missing_number(sequence):
    if sequence=='':
        return 0
    tmp = []
    for i in sequence.split(' '):
        try:
            tmp.append(int(i))
        except:
            return 1
    t = 0
    print(tmp)
    for i in sorted(tmp):
        if t+1 == i:
            t+=1
            continue
        else:
            return t+1
    return 0
