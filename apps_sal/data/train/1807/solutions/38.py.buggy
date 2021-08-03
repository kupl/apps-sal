class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        results = []
        for deno in range(2,n+1):
            for deli in range(1,deno):
                canAdd = True
                for dev in range(2,deli+1):
                    if deno % dev == 0 and deli % dev == 0:
                        canAdd = False
                        break
                if canAdd:
                    results.append(\"{}/{}\".format(deli,deno))
        return results
