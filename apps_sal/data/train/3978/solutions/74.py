def check_for_factor(base, factor):
    # your code here
    remainder = base % factor
    if remainder == 0:
        return True
    else:
        return False
