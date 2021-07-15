def triple_trouble(one, two, three):
    combined = ""
    i = 0
    
    for letter in range(len(one)):
        combined += one[i] + two[i] + three[i]
        i += 1
        
    return combined
