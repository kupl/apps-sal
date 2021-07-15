class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.trie = {}
        
        for path in folder:
            node = self.trie
            for c in path.split('/'):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['*'] = True
            
        res = []
        node = self.trie
        stack = [(node, [])]
        while len(stack):
            node, prefix = stack.pop()
            if '*' in node and node['*']:
                res.append('/'.join(prefix))
            else:
                for k, v in list(node.items()):
                    stack.append((v, prefix+[k]))
                    
        return res

