class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        climb = None
        bef = None
        for num in A:
            if bef is None:
                pass
            elif climb is None and num > bef:
                climb = True
            elif climb is None and num < bef:
                climb = False
            elif climb is None and num == bef:
                pass
            elif climb is True and num >= bef:
                pass
            elif climb is False and num <= bef:
                pass
            else:
                return False
            bef = num
        return True
