class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.trie = {}
        self.pointers = []
        
        for word in words:
            curr = self.trie
            for char in word + '0':
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]

    def query(self, letter: str) -> bool:
        
        new_pointers = []
        hasFound = False
        
        for pointer in self.pointers:
            if letter in pointer:
                new_pointers.append(pointer[letter])
        
        if letter in self.trie:
            new_pointers.append(self.trie[letter])
        
        self.pointers = new_pointers
        
        for pointer in self.pointers:
            if '0' in pointer:
                return True
        
        return False

