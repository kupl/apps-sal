def goto(level, button):
    try:
        return int(button) - level if button in "0123" and level in {0, 1, 2, 3} else 0
    except (TypeError, ValueError):
        return 0
