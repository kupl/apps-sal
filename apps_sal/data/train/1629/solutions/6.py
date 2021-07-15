def lsorter2(l):
    intsec = [(a,b) for (a,b) in zip(l, sorted(l)) if a!=b]
    return list(zip(*intsec))

def naturalSwap(l):
    x1 = lsorter2(l)
    ori = list(x1[0])
    sort = list(x1[1])

    si = [i for i, x in enumerate(sort) if x == ori[0]]
    fi = [i for i, x in enumerate(ori) if x == sort[0]]

    ci = [x for x in si if x in fi]

    new_ori = [x for i,x in enumerate(ori) if i not in ci]

    swap_num1 = len(ci)

    si2 = [i for i, x in enumerate(ori) if x == ori[0]]
    fi2 = [i for i, x in enumerate(sort) if x == sort[0]]

    ci2 = [x for x in si2 if x in fi2]

    new_ori2 = [x for i,x in enumerate(ori) if i not in ci2]

    swap_num2 = len(ci2)

    swap_real= min(swap_num1,swap_num2)

    to_force_swap1 = ci[:swap_real]
    to_force_swap2 = ci2[:swap_real]

    to_force_swap3 = to_force_swap1 + to_force_swap2

    new_list = [x for i, x in enumerate(ori) if i not in to_force_swap3]
    return (new_list, swap_real)

def forcedSwap(l):
    x1 = lsorter2(l)
    ori = list(x1[0])
    sort = list(x1[1])

    idx = ori.index(sort[0])
    ori[0], ori[idx] = ori[idx], ori[0]
    return ori



def exchange_sort(l):
    swaps = 0
    dlist = l[:]
    cnt = 1
    if dlist == sorted(dlist):
        return 0
    
    else:
        while cnt > 0 and len(dlist) > 0:
            cnt = 0
            x1 = naturalSwap(dlist)
            cnt = x1[1]
            swaps += x1[1]
            dlist = x1[0]
        while len(dlist) > 2:
            x2 = forcedSwap(dlist)
            swaps+=1
            dlist = x2
        return swaps

