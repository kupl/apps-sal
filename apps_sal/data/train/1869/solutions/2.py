# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S: 
            return None
        if len(S) == 1: 
            return TreeNode(int(S))
        
        def split_str(S): 
            S += '-'
            ls = []
            start = 0
            for i in range(1, len(S)):
                if (S[i] == '-') & (S[i - 1] != '-'): 
                    ls.append(S[start: i])
                    start = i
            return ls
        
        ls_nodes = split_str(S)
        
        def build_tree(ls): 
            if not ls: 
                return None
            root = TreeNode(int(ls[0]))
            if len(ls) == 1: 
                return root
            
            lft = [ls[1][1:]]
            rgt = []
            flag = 0
            for i in range(2, len(ls)):
                if ls[i][1] != \"-\": 
                    flag = 1
                    rgt.append(ls[i][1:])
                else: 
                    if flag == 0: 
                        lft.append(ls[i][1:])
                    else: 
                        rgt.append(ls[i][1:])
                        
            root.left = build_tree(lft)
            root.right = build_tree(rgt)
            
            return root
        
        return build_tree(ls_nodes)
                    
        
