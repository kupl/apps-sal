# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


visited = set()


def dfs(cloned, target):

    if cloned.val not in visited:
        # print(f\"looking at {cloned}\")
        visited.add(cloned)
        # print(f\"added {cloned} to visited\")

        if cloned.val == target.val:
            # print(f\"Found the target! {cloned}\")
            # print(\"Returning cloned...\")
            print(cloned)
            return cloned

        if cloned.left:
            # print(\"calling dfs on cloned.left\")
            a = dfs(cloned.left, target)
            if a:
                return a

        if cloned.right:
            # print(\"calling dfs on cloned.right\")
            a = dfs(cloned.right, target)
            if a:
                return a


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # print(f\"original {original}\")
        # print(f\"cloned {cloned}\")
        # print(f\"target {target}\")

        found = dfs(cloned, target)

        # print(f\"found: {found}\")

        return found
