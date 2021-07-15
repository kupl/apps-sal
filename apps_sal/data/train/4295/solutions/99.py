def balanced_num(number):  
    l = str(number)[:(len(str(number)) +1 )// 2 - 1]
    r = str(number)[(len(str(number)))// 2 + 1:]
    if sum([int(x) for x in l]) == sum([int(x) for x in r]):
        return "Balanced"
    return "Not Balanced"
