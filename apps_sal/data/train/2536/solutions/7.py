class Solution:

    def findLucky(self, arr: List[int]) -> int:
        out = -1
        for (key, value) in list(Counter(arr).items()):
            if key == value and value > out:
                out = value
        return out
