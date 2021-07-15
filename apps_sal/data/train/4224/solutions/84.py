def dont_give_me_five(start,end):
    # your code here
    return len([t for t in range(start,end+1) if str(t).find("5") == -1])
