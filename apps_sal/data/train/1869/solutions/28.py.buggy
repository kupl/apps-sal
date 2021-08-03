# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def split(S, split_depth):
            split_index = -1
            i = len(S) - 1
            while i >= 0:
                temp_depth, size = i, 0
                while temp_depth < len(S) and S[temp_depth] == \"-\":
                    temp_depth -= 1
                    size += 1
                if size == split_depth:
                    split_index = temp_depth
                    break
                i = temp_depth
                i -= 1
            return split_index
        
        
        def process(S):
            node = None
            if len(S) != 0:
                depth = 0
                while depth < len(S) and S[depth] == \"-\":
                    depth += 1
                num = depth
                while num < len(S) and S[num].isdigit():
                    num += 1
                number = S[depth : num]
                node = TreeNode(int(number))
                S = S[num:]
                split_depth = depth + 1
                split_index = split(S, split_depth)
                if split_index != -1:
                    left, right = S[:split_index + 1], S[split_index + 1:]
                    node.left, node.right = process(left), process(right)
                else:
                    node.left, node.right = process(S), None                 
            return node
        return process(S)
