# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# do not assume binary trees are balanced or sorted!

LEFT_PROCESSED = 1
RIGHT_PROCESSED = 2

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def recurse_func(node, parent_vals, best_answer):
            # check if we can compute a better answer with this node
            if parent_vals:
                ans = abs(min(parent_vals) - node.val)
                if ans > best_answer:
                    best_answer = ans
                ans = abs(max(parent_vals) - node.val)
                if ans > best_answer:
                    best_answer = ans
            
            # check our children
            # there is some optimization that can occur here to prune entire branches if we detect the best answer is larger
            # than the largest value we expect to find in the tree branch, but we would need to record whether we came down the left or right branch of the parent
            parent_vals.append(node.val)
            if node.left:
                best_answer = recurse_func(node.left, parent_vals, best_answer)
            if node.right:
                best_answer = recurse_func(node.right, parent_vals, best_answer)
            parent_vals.pop()
            
            # return best_answer
            return best_answer
    
        return recurse_func(root, [], 0)

    
#         best_answer = 0
#         parent_nodes = [[root, 0]]
#         while parent_nodes:
#             cn = parent_nodes[-1]
#             for n in parent_nodes:
#                 ans = abs(n[0].val - cn[0].val)
#                 if ans > best_answer:
#                     best_answer = ans

#             n = cn[0]                    
#             if not (cn[1] & LEFT_PROCESSED):
#                 cn[1] = cn[1] | LEFT_PROCESSED
#                 if n.left:
#                     parent_nodes.append([n.left, 0])
#                 continue
#             if not (cn[1] & RIGHT_PROCESSED):
#                 cn[1] = cn[1] | RIGHT_PROCESSED
#                 if n.right:
#                     parent_nodes.append([n.right, 0])
#                 continue
#             if (cn[1] & LEFT_PROCESSED) and (cn[1] & RIGHT_PROCESSED):
#                 parent_nodes.pop()
#         return best_answer
        
    
                

