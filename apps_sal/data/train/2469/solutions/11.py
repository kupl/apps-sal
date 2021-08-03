class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for e in arr:
            if 2 * e in seen or (e % 2 == 0 and e // 2 in seen):
                return True
            seen.add(e)
        return False
