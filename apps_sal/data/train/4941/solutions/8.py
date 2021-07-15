def lineup_students(s):
    return sorted(s.strip().split(" "), key=lambda x:(len(x), x), reverse=True)
