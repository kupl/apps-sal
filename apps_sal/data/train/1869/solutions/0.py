# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        itera = re.finditer(r'(-*)(\\d+)', S)
        
        root = TreeNode(int(next(itera).group(2)))
        
        tofill = [root]
        
        for m in itera:
            k = len(m.group(1))
            if k == len(tofill):
                node = TreeNode(int(m.group(2)))
                tofill[-1].left = node
                tofill.append(node)
            else:
                node = TreeNode(int(m.group(2)))
                tofill[k-1].right = node
                tofill[k:] = [node]
        
        return root
