def membership(amount, platinum, gold, silver, bronze):
    import inspect
    frame = inspect.currentframe()
    (args, _, _, values) = inspect.getargvalues(frame)
    if amount < values[args[4]]:
        return 'Not a member'
    elif amount < values[args[3]]:
        return ''.join([chr(66), chr(114), chr(111), chr(110), chr(122), chr(101)])
    elif amount < values[args[2]]:
        return ''.join([chr(83), chr(105), chr(108), chr(118), chr(101), chr(114)])
    elif amount < values[args[1]]:
        return ''.join([chr(71), chr(111), chr(108), chr(100)])
    else:
        return ''.join([chr(80), chr(108), chr(97), chr(116), chr(105), chr(110), chr(117), chr(109)])
