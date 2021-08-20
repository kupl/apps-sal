def find_deleted_number(a, m):
    return next((e for e in set(a) - set(m)), 0)
