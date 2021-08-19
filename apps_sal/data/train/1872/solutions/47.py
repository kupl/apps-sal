# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        levelMapping = {}
        queue = []
        queue.append([root, 1])
        while queue:
            s = queue.pop(0)

            if s[0] == None:
                continue

            if s[1] in levelMapping:
                if levelMapping[s[1]]:
                    levelMapping[s[1]] += s[0].val
            else:
                levelMapping[s[1]] = s[0].val
            queue.append([s[0].left, s[1] + 1])
            queue.append([s[0].right, s[1] + 1])
        maximum = -999999999999999999999
        maximum_level = 0
        print(levelMapping)
        for key in levelMapping:
            if levelMapping[key] and maximum < levelMapping[key]:
                maximum = levelMapping[key]
                maximum_level = key
        return maximum_level
