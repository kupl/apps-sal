class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A) >= 3):
            peak = max(A)
            if(A.count(peak) == 1):
                peakInd = A.index(peak)
                incArr = A[:peakInd]
                decArr = A[peakInd + 1:]
                if(len(incArr) > 0 and len(decArr) > 0):
                    for i in range(1, len(incArr)):
                        if(incArr[i] <= incArr[i - 1]):
                            return False
                    for d in range(0, len(decArr) - 1):
                        if(decArr[d] <= decArr[d + 1]):
                            return False
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
