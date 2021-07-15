from itertools import permutations as p

def rearranger(k, *args):
    res, u, t = 1E200, len(args),(0,0)
    for i in p(args,u):
        a = int(''.join(map(str,i)))
        if a % k == 0:
            if a < res:
                res = a
                t = i
            if a == res:
                if i < t:
                    t = i
    if t == (0,0):
        return "There is no possible rearrangement"
    else:
        return "Rearrangement: " + str(t)[1:-1] + " generates: " + str(res) + " divisible by " + str(k)
