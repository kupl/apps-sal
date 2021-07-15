class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.folders = {}
        self.exist = False
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        self.tree = TreeNode('.')
        for this_folder in folder:
            path = this_folder.split('/')[1:]
            pointer = self.tree
            for name in path:
                if pointer.exist:
                    break
                if name not in pointer.folders:
                    pointer.folders[name] = TreeNode(name)
                pointer = pointer.folders[name]
            pointer.exist = True
        
        ret = []
        
        # print(self.tree)
        # print(self.tree.folders)
        # print(self.tree.folders['a'].folders)
        # print(self.tree.folders['a'].exist)
        
        def buildPath(curr, path):
            if curr is None:
                return
            if curr.exist:
                ret.append(path)
                return
            for sub_name, sub in curr.folders.items():
                buildPath(sub, path + '/' + sub_name)
        
        buildPath(self.tree, '')
        return ret
