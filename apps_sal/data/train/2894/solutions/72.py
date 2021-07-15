def triple_trouble(one, two, three):
    result = ''
    counter = 0
    while counter < len(one):
        result += one[counter] + two[counter] + three[counter]
        counter += 1
    return result
