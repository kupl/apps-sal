from itertools import permutations

def rearranger(k, *args):
    perms = permutations(map(str, args), len(args))
    divisible_by_k = filter(lambda x: int(''.join(x)) % k == 0, perms)
    try:
        rearranged = min(divisible_by_k, key=lambda x: int(''.join(x)))
        return 'Rearrangement: {} generates: {} divisible by {}'.format(', '.join(rearranged), ''.join(rearranged), k)
    except ValueError:
        return "There is no possible rearrangement"
