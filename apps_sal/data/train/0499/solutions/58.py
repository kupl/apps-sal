import heapq

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        stack = [(0, -1)]
        ans = 0
        for i, x in enumerate(target):
            if stack[-1][0] < x:
                stack.append((x, i))
            elif stack[-1][0] == x:
                stack[-1] = (stack[-1][0], i)
            else:
                while len(stack) >= 2 and stack[-1][0] >= x:
                    tmp = stack.pop()
                    ans += tmp[0] - max(x, stack[-1][0])
                    if stack[-1][0] > x:
                        stack[-1] = (stack[-1][0], tmp[1])
                stack.append((x, i))
                
        return ans
                    

