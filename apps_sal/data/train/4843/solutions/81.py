from itertools import combinations 

def choose_best_sum(t, k, ls):
    uniqueCombinations = list(combinations(ls, k))
    
    sumOfCombos = []
    for tup in uniqueCombinations:
        tupSum = sum(list(tup))
        
        if tupSum <= t:
            sumOfCombos.append(tupSum)
    if len(sumOfCombos) == 0:
        return None
    else:
        return min(sumOfCombos, key=lambda x:abs(x-t))

