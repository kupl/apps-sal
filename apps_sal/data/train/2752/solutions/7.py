def summary_ranges(a):
    a,i,li = sorted(set(a), key=a.index),0,[]
    while i < len(a):
        temp = [a[i]] ; i += 1
        while i < len(a) and temp[-1] + 1 == a[i] : temp.append(a[i]) ; i += 1
        li.append(temp)
    return [f"{i[0]}->{i[-1]}" if len(i) > 1 else f"{i[0]}" for i in li]
