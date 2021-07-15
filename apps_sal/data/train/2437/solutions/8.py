class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        L = len(arr)
        for i in range(L - m * k + 1):
            offset = 0
            iFlag = True
            for ki in range(1, k):
                offset += m
                kFlag = True
                for mi in range(m):
                    if arr[i + mi] != arr[i + offset + mi]:
                        kFlag = False
                        break
                if not kFlag:
                    iFlag = False
                    break
            if iFlag:
               return True
        return False

