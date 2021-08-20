def avoid(rains):
    zeros = []
    full = {}
    sol = [-1] * len(rains)
    for (ix, r) in enumerate(rains):
        if r == 0:
            zeros.append(ix)
        elif r not in full:
            full[r] = ix
        else:
            if not zeros:
                return []
            zix = None
            rix = full[r]
            for i in range(len(zeros)):
                if zeros[i] > rix:
                    zix = zeros.pop(i)
                    break
            if not zix:
                return []
            sol[zix] = r
            full[r] = ix
    while zeros:
        sol[zeros.pop()] = 1
    return sol


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        return avoid(rains)
