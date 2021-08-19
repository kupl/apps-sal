def work_needed(mins, free):
    w = mins - sum((60 * h + m for (h, m) in free))
    return f'I need to work {w // 60} hour(s) and {w % 60} minute(s)' if w > 0 else 'Easy Money!'
