class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # seen = set()
        # for e in arr:
        #     if 2*e in seen or (e % 2 == 0 and e//2 in seen):
        #         return True
        #     seen.add(e)
        # return False
    
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == 2*arr[j] or arr[j] == 2*arr[i]:
                    return True
        return False
    
        # for e in arr:
        #     if 2*e in arr:
        #         return True
        # return False

