# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if S == '':
            return
        root = TreeNode(S.split('-')[0])
        stack = [(root, 0)]
        nodes = []
        i = len(root.val)
        depth = 0
        val = []
        started = False
        while i < len(S):
            if S[i] == '-':
                if started:
                    nodes.append((TreeNode(''.join(val)), depth))
                    depth = 0
                    val = []
                    started = False
                depth += 1
            else:
                started = True
                val.append(S[i])
            i += 1
        nodes.append((TreeNode(''.join(val)), depth))
        print(nodes)
        for node in nodes:
            while len(stack) > 0 and node[1] <= stack[-1][1]:
                stack.pop()
            if len(stack) > 0:
                parent = stack[-1][0]
                if parent.left is None:
                    parent.left = node[0]
                else:
                    parent.right = node[0]
            stack.append(node)
        return root
