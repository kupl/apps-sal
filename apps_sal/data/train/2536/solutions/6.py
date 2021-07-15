class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = [-1]
        for num, keys in list(Counter(arr).items()):
            if num == keys:
                lucky.append(num)
        return max(lucky)

