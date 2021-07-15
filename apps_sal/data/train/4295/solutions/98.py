def balanced_num(number): 
    if sum([int(x) for x in str(number)[:(len(str(number)) +1 )// 2 - 1]]) == sum([int(x) for x in str(number)[(len(str(number)))// 2 + 1:]]):
        return "Balanced"
    return "Not Balanced"
