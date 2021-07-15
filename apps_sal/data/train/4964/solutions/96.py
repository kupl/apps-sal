def is_uppercase(inp):
    count_lower = 0
    for i in inp:
        if i.islower():
            count_lower += 1
    if count_lower > 0:
        return False
    else:
        return True
