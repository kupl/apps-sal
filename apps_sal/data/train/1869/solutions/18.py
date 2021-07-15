# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        dashes = 0
        stk = []
        i = 0
        while i < len(S):
            s = S[i]
            if s.isnumeric():
                c = s
                while i+1 < len(S) and S[i+1].isnumeric():
                    c += S[i+1]
                    i += 1
                while stk and dashes != stk[-1][1] + 1:
                    stk.pop()
                
                node = TreeNode(int(c))
                if stk and stk[-1][0].left:
                    stk[-1][0].right = node
                elif stk: stk[-1][0].left = node
                stk.append((node, dashes))
                dashes = 0
            
            else:
                dashes += 1
            
            i += 1
                
        return stk[0][0]
        
#         dashes = 0
#         node_depths = collections.defaultdict(list)
        
#         #root = TreeNode(int(S[0])))
#         expected_dashes = 1
        
#         for s in S:
#             if s.isnumeric():
#                 node_depths[dashes].append(int(s))
#                 dashes = 0
            
#             else:
#                 dashes += 1
        
#         stk = [TreeNode(int(S[0]))]
#         del node_depths[0]
#         for depth in sorted(node_depths):
#             for child in node_depths[depth]:
#                 if depth == 
            
        
        
        
        
        
#         traversal = [d for depth in sorted(node_depths) for d in node_depths[depth]]
#         print(traversal)
#         return traversal
    
        

