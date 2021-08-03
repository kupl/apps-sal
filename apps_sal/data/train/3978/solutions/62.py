def check_for_factor(base, factor):
    # i take the parameters and convert in integer
    base = int(base)
    factor = int(factor)
#     here checking if the mod would evaluate to 0
    if base % factor == 0:
        return True
    else:
        return False
