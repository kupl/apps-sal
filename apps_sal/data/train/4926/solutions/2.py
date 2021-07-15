def only_one(*args):
    count = 0
    for item in args:
        if item:
            count += 1
        if count == 2:
            return False
    return True if count == 1 else False
