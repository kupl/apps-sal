def check(seq, elem):
    for nums in seq:
        if nums == seq or nums == elem:
            return True
    return False
