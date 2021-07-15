def modes(data):
    #making a dictionary with every symbol as key and numbers it's used in given data as value
    dict = {i: data.count(i) for i in data}

    #if there are at least two symbols used different number of times in data
    if max(dict.values()) != min(dict.values()): 
        #we return sorted list with symbols used maximum times in data in it (list of modes)
        return sorted([key for key, value in dict.items() if value == max(dict.values())])
    
    return []
