def triple_trouble(one, two, three):
    strin = ''
    
    for el in range(len(one)):
        strin += one[el] + two[el] + three[el]
    
    return strin
