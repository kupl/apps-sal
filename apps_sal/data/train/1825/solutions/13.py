# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def __init__(self):
        self.mapper = {}

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        self.traverse_tree(root, [])

        for key, vals in self.mapper.items():
            print(f'{key}: {[item.val for item in vals]}')

        lst_of_nodes = list(self.mapper.values())
        if len(lst_of_nodes) == 1:
            return lst_of_nodes[0][-1]

        common = None
        length = max(map(len, lst_of_nodes))

        for i in range(length):
            curr = None
            for nodes in lst_of_nodes:
                if len(nodes) < length:
                    continue
                if not curr:
                    curr = nodes[i]
                    continue
                if curr == nodes[i]:
                    continue
                else:
                    return common
            common = curr
        return common

    def traverse_tree(self, node: TreeNode, ancestors: list) -> None:
        if not node:
            return
        new_lst = ancestors.copy()
        new_lst.append(node)
        if not node.left and not node.right:
            self.mapper[node.val] = new_lst

        self.traverse_tree(node.left, new_lst)
        self.traverse_tree(node.right, new_lst)
