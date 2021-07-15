def alex_mistakes(number_of_katas, time_limit):
    req_time = 5
    sets = 0
    remaining = time_limit - number_of_katas * 6
    
    while remaining>=req_time:
        remaining-=req_time
        req_time*=2
        sets+=1
        
    return sets
