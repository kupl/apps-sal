# You can just do "int(st) % 3 == 0"

def divisible_by_three(st): 
    while len(st) > 1:
        st = str(sum(map(int, st)))
    return st in "369"
