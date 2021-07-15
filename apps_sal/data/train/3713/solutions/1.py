def find_deleted_number(a, b):
    return (set(a) - set(b)).pop() if len(a) != len(b) else 0
