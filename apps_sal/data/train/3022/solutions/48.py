def two_highest(arg1):
    new = set(arg1)
    final_list = list(new)
    final_list.sort()
    if len(final_list) == 1:
        return final_list
    elif final_list == []:
        return final_list

    highest = [final_list[-1], final_list[-2]]
    
    return highest
    

