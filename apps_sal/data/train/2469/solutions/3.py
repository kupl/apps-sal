class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        tracker = set()
        for n in arr:
            if (n % 2 == 0 and (n / 2) in tracker) or n * 2 in tracker:
                return True
            tracker.add(n)
        return False
