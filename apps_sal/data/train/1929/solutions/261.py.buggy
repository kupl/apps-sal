class StreamChecker:

    \"\"\"
    cd, f, kl, 
           ^
    
    
    trie{
        d: {
            c: {
                $: True
            }
            },        
        f: {
            $: True   
            }        
        k: {
          l: {
            $: True
            }
            }
    }
    
    queue = [a, b, c, d]
                      ^
                      
            dcba
            ^
    \"\"\"
    def __init__(self, words: List[str]):
        self.trie = {} 
        self.stream = []
        for word in words:
            node = self.trie
            for letter in reversed(word):
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['$'] = True                        

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        for letter in reversed(self.stream):            
            if letter in node:
                node = node[letter]
                if \"$\" in node:
                    return True
            else:
                return False
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
