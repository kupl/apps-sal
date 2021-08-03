def check_for_factor(base, factor):
    # your code here
    a = base % factor
    if a == 0:
        return True
    else:
        return False
