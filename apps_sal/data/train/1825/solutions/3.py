from typing import Tuple


class Solution:

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def lcaDeepestLeavesRecursive(node: TreeNode) -> Tuple[int, TreeNode]:
            if node is None:
                return (0, None)
            else:
                (depthL, nodeL) = lcaDeepestLeavesRecursive(node.left)
                (depthR, nodeR) = lcaDeepestLeavesRecursive(node.right)
                if depthL > depthR:
                    return (depthL + 1, nodeL)
                elif depthL < depthR:
                    return (depthR + 1, nodeR)
                else:
                    return (depthL + 1, node)
        return lcaDeepestLeavesRecursive(root)[1]
