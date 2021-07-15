def target_game(values):
    values[2] = get_highest_possible_score(0, values[0], values[2]) 
    for i in range(3,len(values)):
        values[i] = get_highest_possible_score(values[i-3], values[i-2], values[i]) 
    return max(values)

def get_highest_possible_score(a,b,n):
    a = max(0,a)
    b = max(0,b)
    n = max(0,n)
    
    if(a>b):
        return a+n

    return b+n
