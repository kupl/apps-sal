class Solution1:
    # brute force
    def minNumberOperations(self, target: List[int]) -> int:
        max_bar, blocks = max(target), 0
        for bar in range(1, max_bar + 1):
            op = [ 0 ] * len(target)
            prev_op = 0
            for i, t in enumerate(target):
                if t >= bar:
                    op[i] = 1
                if prev_op != op[i]:
                    prev_op = op[i]
                    if op[i] == 1:
                        blocks += 1     
        return blocks
    
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev_t, n, valley = 0, len(target), 0
        blocks = 0
        for i in range(n):
            if i + 1 < n and target [i + 1] == target[i]:
                continue
            if prev_t < target[i] and (i + 1 == n or target[i] > target[i + 1]):
                blocks += target[i] - valley
            if target[i] <  prev_t and (i + 1 == n or target[i] <= target[i+1]):
                valley = target[i]
            prev_t = target[i]     
        return blocks
            
            

