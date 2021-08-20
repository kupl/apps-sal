class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = []
        lastNumberSet = set([start ^ 1 << i for i in range(n)])
        nMax = 2 ** n
        visited = set()
        visited.add(start)

        def helper(preNum, ni):
            if ni == nMax:
                if preNum in lastNumberSet:
                    return True
                return False
            for i in range(n):
                nextNum = preNum ^ 1 << i
                if nextNum not in visited:
                    visited.add(nextNum)
                    if helper(nextNum, ni + 1):
                        ans.append(nextNum)
                        return True
                    visited.remove(nextNum)
            return False
        helper(start, 1)
        return [start] + ans[::-1]
