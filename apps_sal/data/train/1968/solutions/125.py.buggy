class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if len(folder) == 1:
            return folder
        
        trie = {}
        for p in folder:
            node = trie
            p = p.split('/')
            for e in p:
                node = node.setdefault(e, {}) 
            node[\"#\"] = \"#\" #end
        
        restults = []
        self.dfs(trie, [], restults )
        return restults
            
        
    def dfs(self, trie, res, results):
        
        if '#' in trie:
            results.append('/'.join(res)) 
            return
               
        for e in trie:
            self.dfs(trie[e], res + [e], results)
            
            
        
        
            
            
            
        
        
            
            
        
