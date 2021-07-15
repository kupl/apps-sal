def goto(level,button):
    if type(level) is not int or level>3 or type(button) is not str or int(button)>3:
        return 0
    return int(button)-level

