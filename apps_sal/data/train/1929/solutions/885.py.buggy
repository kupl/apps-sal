class StreamChecker:

    def construct_trie(self, word_list):
        root = dict()
        for word in word_list:
            word += \"_\"
            level = root
            for letter in word:
                if letter not in level:
                    level[letter] = dict()
                level = level[letter]
        return root
    
    def __init__(self, words: List[str]):
        self.liste = self.construct_trie(words)
        self.p = [self.liste]
        

    def query(self, letter: str) -> bool:
        ll = [self.liste]
        b = False
        for dic in self.p:
            if letter in dic:
                d = dic[letter]
                if \"_\" in d:
                    b = True
                ll.append(d)
        self.p = ll
        return b
