class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        stack = []
        
        for char in S:
            
            if char not in stack or char != stack[-1]:
                stack += [char]
            
            else:
                stack = stack[: -1]
            #print(stack)
            
        return ''.join(stack)

