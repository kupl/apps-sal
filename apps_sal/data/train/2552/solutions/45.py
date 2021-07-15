class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)/4
        freq ={}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for k, v in list(freq.items()):
            if v > n:
                return k

