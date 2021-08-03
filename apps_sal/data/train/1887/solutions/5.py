class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        n = len(M)
        seen = set()
        groups = 0

        for idx in range(n):
            if idx not in seen:
                # print(idx)
                groups += 1
                seen.add(idx)
                front = {idx}
                while len(front) > 0:
                    #print(front, seen)
                    newFront = set()
                    for cIdx in front:
                        for fIdx in range(n):
                            if M[cIdx][fIdx] == 1 and fIdx not in seen:
                                seen.add(fIdx)
                                newFront.add(fIdx)
                    front = newFront
        return groups
