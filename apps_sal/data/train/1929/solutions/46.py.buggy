class Trie:
    \"\"\"
    Keeps the list of Node, as entry point, using hashing.
    \"\"\"
    nodes = {}
    
class Node:
    char_id = None
    end = False
    next_char_ids = []
    
class StreamChecker:
    def __init__(self, words: List[str]):
        # self.char_set = set()
        # for word in words:
        #     self.char_set = self.char_set.union(iter(word))
        self.trie = self.build_trie(words)
        self.curr_tries = []
        
    def build_trie(self, words):
        \"\"\"
        Building reverse trie can be usable for 
        suffix search.
        \"\"\"
        trie = {}
        for word in words:
            c = word[0]
            if c in trie:
                trie_tmp = trie[c]
            else:
                trie[c] = {}
                trie_tmp = trie[c]

            for c in word[1:]:
                if c not in trie_tmp:
                    trie_tmp[c] = {}
                trie_tmp = trie_tmp[c]
            trie_tmp[\"ends\"] = True
        return trie        
    
    def query(self, char) -> bool:
        \"\"\"
        Keep the Trie Tree traversal pointer.
        \"\"\"
        if char in self.trie:
            self.curr_tries.append(self.trie)
        
        new_curr_tries = []
        a_word = False
        for ind, curr_trie in enumerate(self.curr_tries):
            if char in curr_trie:
                curr_trie[char] and new_curr_tries.append(curr_trie[char])
                # Once it turns positive, stay positive. Means one of the
                # trie path, we found word boundary.
                a_word = a_word or \"ends\" in curr_trie[char]
        self.curr_tries = new_curr_tries
        return a_word
        
    def query1(self, char: str) -> bool:
        if self.curr_trie:
            if char in self.curr_trie:
                a_word = \"ends\" in self.curr_trie[char]
                self.curr_trie = self.curr_trie[char]
                return a_word
            else:
                self.curr_trie = {}
                return False
        else:
            # Address the chance of single char only words.
            self.curr_trie = self.trie.get(char, {})
            return \"ends\" in self.curr_trie
        
        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
