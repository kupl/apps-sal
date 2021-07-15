from itertools import permutations

def rearranger(k, *args):
    options = sorted(permutations(args, len(args)), key=lambda option: (''.join(str(x) for x in option), option))
    res = "There is no possible rearrangement"
    for option in options: 
        aux = int(''.join(str(x) for x in option))
        if aux%k==0: 
            res = "Rearrangement: {} generates: {} divisible by {}".format(', '.join(str(x) for x in option), aux, k)
            break
    return res

