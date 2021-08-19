def work_needed(pm, fls):
    pm -= sum((60 * h + m for (h, m) in fls))
    return f'I need to work {pm // 60} hour(s) and {pm % 60} minute(s)' if pm > 0 else 'Easy Money!'
