def reverse_invert(lst):
    step1 = [str(-1 * int(str(n)))[::-1] for n in lst if type(n) == int]
    step2 = [int(x) if '-' not in x else -1 * int(x.replace('-', ''))for x in step1]
    return step2
