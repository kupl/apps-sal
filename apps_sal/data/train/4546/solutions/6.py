def find_children(db):
    return ''.join(sorted(db, key=lambda a: (a.upper(), a)))
