import numpy as np 

def number_to_bin_array(a, k, digits):
    b = bin(a)
    arr = []
    one_count = 0
    while a != 0:
        val = a%2
        if val == 1:
              one_count += 1
        if one_count > k:
            return None
        arr.append(a%2)
        a = int(a/2)
    if one_count < k:
        return None
    for i in range(digits - len(arr)):
        arr.append(0)
    arr.reverse()
    return arr

def choose_best_sum(t, k, ls):
    if len (ls) < k:
        return None
    ls_f = np.array(ls) 
    ls_f.sort();
    
    min_sum = 0
    for i in range(0, k - 1):
         min_sum += ls_f[i]
    indices = []
    for l in range(0, len(ls_f)):
        if ls_f[l] > t - min_sum:
            indices.append(l)
    
    ls_f = np.delete(ls_f, indices)
    if len (ls_f) < k:
        return None
    town_count = len(ls_f)
    m = 1<<town_count
    
    max_dist = 0
    for mask in range (0, m):
        n = number_to_bin_array(mask, k, town_count)
        if n == None:
            continue
        sum = 0
        for i in range (0, len(n)):
            if n[i] == 1:
                sum+=ls_f[i]
        if sum <= t and sum > max_dist:
             max_dist = sum
    if max_dist == 0:
        return None
    return max_dist
