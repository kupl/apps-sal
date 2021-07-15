def choose_best_sum(t, k, ls):
    solutions = set()
    recursive_search(t, k, 0, ls, 0, 0, solutions)
    if len(solutions)>0:
        return max(solutions)
    else:
        return None
    
def recursive_search(t, maxk, k, ls, ind, solution, solutions):
    if ind == len(ls) or k==maxk or maxk - k > len(ls) - ind:
        return
    recursive_search(t, maxk, k, ls, ind+1, solution, solutions)
    k += 1
    solution += ls[ind]
    if solution <= t:
        if k == maxk:
            if solution in solutions:
                return
            solutions.add(solution)
            return
        recursive_search(t, maxk, k, ls, ind+1, solution, solutions)
