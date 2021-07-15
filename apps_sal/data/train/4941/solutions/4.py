def lineup_students(stg):
    return sorted(sorted(stg.split(), reverse=True), key=len, reverse=True)
