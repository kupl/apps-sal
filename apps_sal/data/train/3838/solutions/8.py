def goto(level, button): return 0 if level not in [0, 1, 2, 3] or button not in ['0', '1', '2', '3'] else int(button) - level
