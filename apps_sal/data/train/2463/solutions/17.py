class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        increasing = True
        prev = -1
        if len(A) < 3:
            return False
        for idx, i in enumerate(A):
            print(prev, i, increasing)
            if i == prev:
                return False
            if increasing:
                if i < prev:
                    increasing = False
                    if idx == 1:
                        return False
            else:
                if i > prev:
                    return False
            prev = i
        if increasing == True:
            return False
        return True
