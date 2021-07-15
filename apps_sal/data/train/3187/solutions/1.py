def sum_nested(lst):
    total = 0
    for ele in lst:
        total += ele if type(ele) != list else sum_nested(ele)
        
    return total
