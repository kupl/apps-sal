def dont_give_me_five(start,end):
    count = 0
    for i in range(start,end+1):
        if str(i).__contains__("5"):
            continue
        else:
            count+=1
    return count
