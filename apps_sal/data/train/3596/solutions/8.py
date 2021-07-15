def membership(amount, platinum, gold, silver, bronze):
    import inspect
    args_names = inspect.getfullargspec(membership).args
    
    for level in args_names[1:]: 
        if amount >= locals().get(level): 
            return level.capitalize()
    else: 
        return "Not a member"
