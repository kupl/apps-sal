
class Solution:
    def pathToNode(self, tree: TreeNode, target: TreeNode, path: str) -> str:
        if not tree:
            return ''

        if target == tree:
            return path

        path.append('L')
        p = self.pathToNode(tree.left, target, path)
        if p:
            return p
        del path[-1]

        path.append('R')
        p = self.pathToNode(tree.right, target, path)
        if p:
            return p
        del path[-1]

        return ''

    def nodeAtPath(self, tree: TreeNode, path: str):
        if not path:
            return tree
        elif 'L' == path[0]:
            return self.nodeAtPath(tree.left, path[1:])
        elif 'R' == path[0]:
            return self.nodeAtPath(tree.right, path[1:])
        assert False

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path_to = self.pathToNode(original, target, [])
        return self.nodeAtPath(cloned, path_to)
