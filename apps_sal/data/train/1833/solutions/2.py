# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.counter = 0
        def dfs(root, nodes, depth):
            if not root.left and not root.right:
                heapq.heappush(nodes, (-depth, self.counter, root))
                self.counter += 1
            if root.left:
                dfs(root.left, nodes, depth + 1)
            if root.right:
                dfs(root.right, nodes, depth + 1)
        dfs(root, nodes, 0)
        deepestNodes = []
        foundArr = []
        maxDepth = nodes[0][0]
        while nodes and nodes[0][0] == maxDepth:
            deepestNodes.append(heapq.heappop(nodes)[2])
            foundArr.append(False)
        def helper(root, deepestNodes, foundArr):
            for i in range(len(deepestNodes)):
                if root == deepestNodes[i]:
                    foundArr[i] = True
                    break
            leftArr = foundArr[:]
            rightArr = foundArr[:]
            leftFound = False
            rightFound = False
            if root.left:
                resLeft = helper(root.left, deepestNodes, leftArr)
                leftFound = True
                for i in leftArr:
                    if not i:
                        leftFound = False
                        break
            if root.right and not leftFound:
                resRight = helper(root.right, deepestNodes, rightArr)
                rightFound = True
                for i in rightArr:
                    if not i:
                        rightFound = False
                        break
            found = True
            for i in range(len(foundArr)):
                foundArr[i] = foundArr[i] or leftArr[i] or rightArr[i]
            if leftFound:
                return resLeft
            elif rightFound:
                return resRight
            for i in foundArr:
                if not i:
                    found = False
                    break
            if found:
                return root
            else:
                return None
        return helper(root, deepestNodes, foundArr)
