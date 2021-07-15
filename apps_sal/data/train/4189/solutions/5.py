def highest_value(a, b):
    return max(a, b, key=lambda stg: sum(ord(char) for char in stg))
