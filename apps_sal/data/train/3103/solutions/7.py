def unique(integers):
    return [value for i, value in enumerate(integers) if value not in integers[:i]]
