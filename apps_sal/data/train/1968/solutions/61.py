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
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for fol in folder:
            trie.add(fol)
        
        response = list()
        response_obj = {}
        for fol in folder:
            key = fol[:fol.rindex(\"/\")]
            while key:
                if key in response_obj:
                    break    
                elif trie.has(key):
                    break
                key = key[:key.rindex(\"/\")]
            
            if not key:
                response.append(fol)
                response_obj[fol] = \"\"

        return response
