from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # 1. dfs 38% time
        # stack = []
        # stack.append((original, cloned))
        # while len(stack) > 0:
        #     o, c = stack.pop()
        #     if o == target: # could compare value instead
        #         return c
        #     if o.left is not None: stack.append((o.left, c.left))
        #     if o.right is not None: stack.append((o.right, c.right))
        # return False # not found - impossible
    
    
        # 2. bfs
        dq = deque()
        dq.append((original, cloned))
        while len(dq) > 0:
            o, c = dq.popleft()
            if o == target: # could compare value instead
                return c
            if o.left is not None: dq.append((o.left, c.left))
            if o.right is not None: dq.append((o.right, c.right))
        return False # not found - impossible
    # todo - try recursion implementation

