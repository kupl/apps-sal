class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = dict()
        for word in words:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = dict()
                node = node[c]
            node['.'] = '.'

        self.curs = []

    def query(self, letter: str) -> bool:
        trie, curs = self.trie, self.curs
        
        ans = False
        
        new_curs = []
        for cur in curs:
            if letter in cur:
                new_cur = cur[letter]
                ans = ans or '.' in new_cur
                new_curs.append(new_cur)
                
        if letter in trie:
            new_cur = trie[letter]
            ans = ans or '.' in new_cur
            new_curs.append(new_cur)
        
        self.curs = new_curs

        return ans
