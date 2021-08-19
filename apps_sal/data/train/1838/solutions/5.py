class Solution:

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        res = 0
        l = len(arr)
        curr = -1
        flag = False
        for i in range(l):
            c = arr[i]
            if flag:
                curr = max(curr, c)
                if curr == i:
                    curr = -1
                    res += 1
                    flag = False
            elif c == i:
                res += 1
            else:
                curr = max(curr, c)
                flag = True
        return res
