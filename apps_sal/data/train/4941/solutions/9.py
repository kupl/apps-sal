def lineup_students(string):
    return sorted(string.split(),key=lambda x:(len(x),x),reverse=True)
