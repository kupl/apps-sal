def lineup_students(s):
    return sorted(s.split(), key=lambda x: (len(x), x), reverse=True)
