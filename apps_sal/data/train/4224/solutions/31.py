def dont_give_me_five(start,end):
    return len([elem for elem in range(start,end+1) if '5' not in str(elem) ])
