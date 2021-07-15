
def add(ptr, c, nptrs):
    # scan
    if c in ptr:
        n = ptr[c]
        nptrs.append( n )
        return 'fin' in n
    return False

class StreamChecker:

    def __init__(self, words: List[str]):
        def add(word, i, pos):
            # add to trie
            if i == len(word):
                pos['fin'] = True
                return
            c = word[i]
            if c not in pos:
                pos[c] = { 'with': c }
            add(word, i + 1, pos[c])
            
        self._trie = { 'root': True, 'with': '$' }
        root = self._trie
        for w in words:
            add(w, 0, root)
            
        self._ptrs = []
        self._ptrs.append( root )
        print(\"built\")
        # print(f\"{self._trie}\")

    def query(self, letter: str) -> bool:
        
        found = False
        nptrs = []
        ptrs = self._ptrs
        for p in ptrs:
            if add(p, letter, nptrs):
                found = True
        nptrs.append( self._trie )
        self._ptrs = nptrs
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
