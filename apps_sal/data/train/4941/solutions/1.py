def lineup_students(s):
    return sorted(s.split(), key=lambda i:(len(i),i), reverse=True)

