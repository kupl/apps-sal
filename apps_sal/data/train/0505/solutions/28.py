class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, index, res = [], [], ''
        for i in range(len(s)):
            if s[i] == '(': stack.append((i, s[i]))
            elif s[i] == ')':
                if not stack: index.append(i)
                elif stack[-1][1] == '(': stack.pop()
        
        while stack:
            index.append(stack.pop()[0])
            
        for i in range(len(s)):
            if i not in index: res += s[i]
        
        return res
#         left, right, index = 0, 0, []
#         remove_left, remove_right = 0, 0
#         for i in range(len(s)):
#             if s[i] == '(': left += 1
#             elif s[i] == ')': right += 1
#             if right > left: 
#                 remove_right += 1
#                 right -= 1
#                 index.append(i)
                
#         remove_left = left - right


