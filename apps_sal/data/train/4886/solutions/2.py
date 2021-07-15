def find_dups_miss(arr):
    dups = []; memo = set()
    a = 100000; b = 0; summ = 0
    for i in arr:
        if i in memo:dups.append(i)
        else: 
            if i < a: a = i
            if i > b: b = i
            memo.add(i)
            summ += i
    miss = int((b * (b + 1)/2 - (a) * (a-1)/2) - summ)
    dups.sort()
    return [miss, dups]
