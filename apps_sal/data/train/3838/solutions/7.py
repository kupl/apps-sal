def goto(level, button):
    return level in range(4) and button in list('0123') and int(button) - level
