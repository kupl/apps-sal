def lineup_students(names):
    return sorted(names.split(), key=lambda s: (len(s), s), reverse=True)
