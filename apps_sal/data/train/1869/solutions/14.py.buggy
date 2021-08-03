# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        level_nodes = []
        c = 0
        print()
        for a in re.split(\"(\\d+)\", S):
            if a == '':
                continue
            elif '-' in a:
                c = len(a)
            else:
                level_nodes.append((c, a))
                c = 0

        def build_tree(arr, l, r, h, root):
            # root = arr[l]
            # assert root[0] == h,  f\"next level_nodes should be {h}\"

            kids = []
            for i in range(l, r+1):
                if arr[i][0] == h:
                    kids.append(i)
                if len(kids) == 2:
                    break
            # print(h, l, r, kids)
            if len(kids) == 0:
                return None
            elif len(kids) == 1:
                left = TreeNode(arr[kids[0]][1])
                root.left = left
                return build_tree(arr, kids[0]+1, r, h+1, left)
            else:
                left = TreeNode(arr[kids[0]][1])
                root.left = left
                build_tree(arr, kids[0]+1, kids[1]-1, h+1, left)
                right = TreeNode(arr[kids[1]][1])
                root.right = right
                return build_tree(arr, kids[1]+1, r, h+1, right)
            
        if len(level_nodes) == 0:
            return None        
        # print(level_nodes)
        root = TreeNode(level_nodes[0][1])
        build_tree(level_nodes, 1, len(level_nodes)-1, 1, root)
        return root
