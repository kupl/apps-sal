def lineup_students(string):
    return sorted(string.split(), reverse = True, key = lambda name:(len(name),name))
