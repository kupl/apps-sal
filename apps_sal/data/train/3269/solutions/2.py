def work_needed(projMin, others):
    (h, m) = map(sum, zip(*others))
    needed = projMin - sum((t * c for (t, c) in zip((h, m), (60, 1))))
    return 'Easy Money!' if needed <= 0 else f'I need to work {needed // 60} hour(s) and {needed % 60} minute(s)'
