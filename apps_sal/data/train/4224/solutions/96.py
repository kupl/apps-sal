def dont_give_me_five(start,end):
    no_fives = [str(x) for x in range(start, end+1) if "5" not in str(x)]
    return len(no_fives) 
