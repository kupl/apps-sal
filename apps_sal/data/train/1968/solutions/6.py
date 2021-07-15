class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.finished = False
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Node(\"\")
        for path in folder:
            paths = path.split(\"/\")
            cur = root
            for each in paths:
                if each == \"\":
                    continue
                if each in cur.children:
                    cur = cur.children[each]
                else:
                    new_node = Node(each)
                    cur.children[each] = new_node
                    cur = new_node
                    
            cur.finished = True
                    
        # get all paths from the root to ...
        folders = []
        def collect(root, path):
            path.append(\"/\"+root.val)
            if root.finished:
                folders.append(list(path))
                path.pop()
                return
            for _, child in root.children.items():
                collect(child, path)
            path.pop()
            
        for _, child in root.children.items():
            collect(child, [])
        return [\"\".join(each) for each in folders]
                
            
                
