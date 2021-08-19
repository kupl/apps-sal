class Solution:

    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        freq = []
        luck = []
        for i in range(len(arr)):
            freq.append(arr.count(arr[i]))
            if freq[i] == arr[i]:
                luck.append(arr[i])
        max_luck = -1
        if luck:
            max_luck = max(luck)
        return max_luck
