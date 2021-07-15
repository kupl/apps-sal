def dont_give_me_five(start, end):
    return len(list(i for i in list(range(start, end+1)) if not "5" in str(i)))
