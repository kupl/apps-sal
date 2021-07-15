class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.words_trie = defaultdict(dict)
        
        for word in words:
            trie_node = self.words_trie[word[-1]]
            for letter in word[-2::-1]:
                next_node = trie_node.setdefault(letter, {})
                trie_node = next_node
            trie_node[None] = None
        
        print((self.words_trie))
        self.queries = []

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        
        trie_node = None
        for query_letter in self.queries[::-1]:
            if trie_node is None:
                trie_node = self.words_trie.get(query_letter, {})
            else:
                trie_node = trie_node.get(query_letter, {})
            
            if not trie_node:
                break
            elif None in trie_node:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

