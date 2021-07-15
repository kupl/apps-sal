def get_strings(city):
    
    # convert to lower case alphabet
    city_alpha = "".join(x.lower() for x in city if x.isalpha())
    
    # order of appearance and count
    seen_cnt, order = {}, ""
    for x in city_alpha :
        if x not in seen_cnt :
            seen_cnt[x]=1 
            order += x
        else :
            seen_cnt[x] += 1
    
    # generate output
    output = ""
    for x in order :
        output += ","+x+":"+"*"*seen_cnt[x]
        
    return output[1:]
