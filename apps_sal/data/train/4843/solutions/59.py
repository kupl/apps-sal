from itertools import combinations

def choose_best_sum(t, k, ls):
    sorted_ls = sorted(ls)
    for distance in sorted_ls:
        if distance > t:
            sorted_ls.remove(distance)
        
    if len(sorted_ls) < k:
        return None
    
    comb = combinations(sorted_ls, k)
    sums = []
    for combination in comb:
        if sum(combination) <= t:
            sums.append(sum(combination))
    
    if sums == []:
        return None
    return max(sums)
    
    
            
        
    
        
        

