def membership(amount, platinum, gold, silver, bronze):
    import inspect
    frame = inspect.currentframe()
    (args, _, _, values) = inspect.getargvalues(frame)
    for i in reversed(list(range(1, 5))):
        if i > 1:
            if values[args[i - 1]] > values[args[0]] >= values[args[i]]:
                return args[i].title()
        elif values[args[0]] >= values[args[i]]:
            return args[i].title()
    return 'Not a member'
