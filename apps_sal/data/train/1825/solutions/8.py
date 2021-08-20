class Solution:

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        dic = {}
        explore = [root]
        nextlevel = []
        while explore:
            leaf = explore
            for node in explore:
                if node.left:
                    dic[node.left] = node
                    nextlevel.append(node.left)
                if node.right:
                    dic[node.right] = node
                    nextlevel.append(node.right)
            (explore, nextlevel) = (nextlevel, [])
        newleaf = set()
        while len(leaf) > 1:
            for node in leaf:
                newleaf.add(dic[node])
            (leaf, newleaf) = (newleaf, set())
        for res in leaf:
            return res
