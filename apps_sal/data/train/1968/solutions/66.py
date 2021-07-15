class Trie:
    def __init__(self):
        self.root = {\"*\": \"*\"}

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[\"*\"] = \"*\"

    def has(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]

        return \"*\" in current

class Solution:
    def removeSubfolders(self, folder1: List[str]) -> List[str]:        
        folder = sorted(folder1, key=len) 
        trie = Trie()
        for fol in folder:
            trie.add(fol)
        
        response = set()
        # for fol in reversed(folder):
        for fol in folder:
            key = fol[:fol.rindex(\"/\")]
            while key:
                if trie.has(key):
                    break
                key = key[:key.rindex(\"/\")]
            
            if not key:
                response.add(fol)
                
        del trie
        return response
