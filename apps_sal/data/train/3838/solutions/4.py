def goto(level, button):
    return int(button) - level if isinstance(level, int) and isinstance(button, str) and level >= 0 and level <= 3 and int(button) >= 0 and int(button) <= 3 else 0
