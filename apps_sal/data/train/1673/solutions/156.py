from collections import Counter
class Solution:
    def get_minset(self, l):
        left = []
        right = []
        n = len(l)
        for i in range(n):
            if i == 0:
                left.append(l[i])
                right.append(l[n-i-1])
            else:
                left.append(min(left[-1], l[i]))
                right.append(min(right[-1], l[n-i-1]))
        right = right[::-1]
        res = []
        for i in range(n):
            if i == 0:
                res.append(right[1])
            elif i == n-1:
                res.append(left[n-2])
            else:
                res.append(min(left[i-1], right[i+1]))
        return res

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        last = arr[0]
        maxset = self.get_minset(last)
        for i in range(1, len(arr)):
            tmp = []
            for j in range(len(arr[0])):
                tmp.append(maxset[j]+arr[i][j])
            last = tmp
            maxset = self.get_minset(last)
        return min(last)
                
                

