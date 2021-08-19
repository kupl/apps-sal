class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = set()
        for i in range(2, n + 1):
            for j in range(1, i):
                denom = i
                num = j
                changed = True
                while changed:
                    changed = False
                    for k in range(2, num + 1):
                        if denom % k == 0 and num % k == 0:
                            denom = denom // k
                            num = num // k
                            changed = True
                fractions.add(str(num) + '/' + str(denom))
        return [i for i in fractions]
