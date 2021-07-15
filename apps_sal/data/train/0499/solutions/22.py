class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        d = 0
        base = target[0]
        for i in range(1,len(target)):
            if target[i] == target[i-1]:
                continue
            elif target[i] < target[i-1]:
                if d == 0:
                    d = -1
                if d == 1:
                    d = -1
                    ans += (target[i-1] - base)
            elif target[i] > target[i-1]:
                if d == 0:
                    d = 1
                if d == -1:
                    d = 1
                    base = target[i-1]
        if d == 1:
            ans += (target[-1] - base)
        return ans
            
                

