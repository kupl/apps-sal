# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S: return None
        
        # \"1-2--3--4-5--6--7\"
        
        que = deque()
        root = TreeNode(int(S[0]))
        index = 0
        while index<len(S):
            depth = 0
            val = []
            while index<len(S) and S[index] == \"-\":
                depth += 1
                index += 1
            while index<len(S) and S[index].isnumeric():
                val.append(S[index])
                index += 1
            val = int(\"\".join(val))
            que.append((val, depth))
            
        
        def helper(depth=None):
            if not que: return None
            
            if depth is not None:
                if que[0][1] == depth or que[0][1]<depth: return None
            
            val, d = que.popleft()
            
            root = TreeNode(val)
            root.left = helper(d)
            root.right = helper(d)
            return root
        
        return helper()
