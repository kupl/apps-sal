def goto(level = None,button = None):
    if level not in (0,1,2,3) or button not in ('0','1','2','3'):
        return 0
    else:
        move = int(button) - level
        return move
