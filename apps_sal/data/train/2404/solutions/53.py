class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        arr1 = []
        while len(arr1) <= k:
            if i not in arr:
                arr1.append(i)
                i = i + 1
            else:
                i += 1
        print(arr1)
        return arr1[k - 1]
