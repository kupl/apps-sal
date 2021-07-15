def membership(amount, platinum, gold, silver, bronze):
    import inspect
    args = inspect.getargspec(membership).args
    l = locals()
    return next((a.title() for a in args[1:] if l[args[0]] >= l[a]), 'Not a member')
