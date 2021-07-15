# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def _recoverFromPreorder(s):
            print (''.join(s))
            if not s:
                return

            root = TreeNode(s.pop())
            depth = 0
            while s:
                if s[-1] == '-':
                    s.pop()
                    depth += 1
                else:
                    break
            
            
            var = 0
            index = -1
            for i in range(len(s)-1, -1, -1):
                if s[i] != '-':
                    if var == depth:
                        index = i
                        break
                    var = 0
                else:
                    var += 1
                    
            if index == -1:
                root.left = _recoverFromPreorder(s)
            else:
                root.right = _recoverFromPreorder(s[:index+1])
                root.left = _recoverFromPreorder(s[index+depth+1:])
            
            return root
        
        arr = list(S)
        arr_1 = []
        
        x = ''
        while arr:
            s = arr.pop()
            if s == '-':
                if x:
                    arr_1.append(x)
                arr_1.append(s)
                x = ''
            else:
                x = s + x
                
        if x:
            arr_1.append(x)
            
        return _recoverFromPreorder(arr_1)
