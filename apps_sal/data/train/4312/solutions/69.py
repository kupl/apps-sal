def pick_peaks(lst):
    res = {'pos': [], 'peaks': []}
    idx = 0
    for i in range(1, len(lst) - 1):
        if lst[i] != lst[idx]:
            idx = i
        if idx and lst[idx - 1] < lst[idx] > lst[i + 1]:
            res['pos'].append(idx)
            res['peaks'].append(lst[idx])
    return res
