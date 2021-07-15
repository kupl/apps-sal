def largest_sum(a):
    best_sum = 0 
    current_sum = 0
    for x in a:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
