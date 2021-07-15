class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return []
        
        trie = {}
        for folderPath in folder:
            paths = folderPath.split(\"/\")
            
            node  = trie
            parent = None
            parentExists = False
            for path in paths[:-1]:
                if \"$\" in node:
                    parentExists = True
                    break
                
                if path not in node:
                    node[path] = {}
                
                parent = node
                node = node[path]
            
            if parentExists or \"$\" in node: continue
            
            #print(node, paths[-1])
            node[paths[-1]] = {\"$\": {}}
        
        #print(trie)
        self.res = []
        self.dfs(trie, [])
        return self.res
    
    def dfs(self, node, pathList):
        for key in node:
            if key == \"$\":
                self.res.append(\"/\".join(pathList))
            else:
                pathList.append(key)
                self.dfs(node[key], pathList)
                pathList.pop()
        
            
    
            
                
            
        
        
