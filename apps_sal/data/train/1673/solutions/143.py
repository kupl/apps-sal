class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        iMax = len(arr)
        jMax = len(arr[0])
        
        # sortedIndex = [sorted([(arr[i][j], j) for j in range(jMax)]) for i in range(iMax)]
        dp = {}
        smallest2 = [None for _ in range(iMax)]
        
        def moveDown(preJ, iNow):
            if iNow == iMax:
                return 0

            if (preJ, iNow) in dp:
                return dp[(preJ, iNow)]
            subAns = float('inf')
            if smallest2[iNow] == None:
                temp1 = float('inf')
                temp1Index = None
                temp2 = float('inf')
                temp2Index = None
                for j, val in enumerate(arr[iNow]):
                    subAns = val + moveDown(j, iNow+1)
                    if subAns <= temp1:
                        temp1, temp2 = subAns, temp1
                        temp1Index, temp2Index = j, temp1Index
                    elif subAns <= temp2:
                        temp2 = subAns
                        temp2Index = j
                smallest2[iNow] = [[temp1Index, temp1], [temp2Index, temp2]]
                
            if preJ == smallest2[iNow][0][0]:
                subAns = smallest2[iNow][1][1]
            else:
                subAns = smallest2[iNow][0][1]
            dp[(preJ, iNow)] = subAns
            return subAns
        return moveDown(-1, 0)

