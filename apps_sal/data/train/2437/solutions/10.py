class Solution:

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        l = list(map(str, arr))
        n = len(l)
        for i in range(n - m + 1):
            d = []
            for j in range(i, n, m):
                x = l[j:j + m]
                if len(x) >= m:
                    if d == []:
                        d.append(x)
                    elif d[-1] == x:
                        d.append(x)
                        if len(d) >= k:
                            return True
                    else:
                        d = [x]
        return False
