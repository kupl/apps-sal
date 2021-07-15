class StreamChecker:

    def __init__(self, words: List[str]):
        self.suffixTree = {}
        
        for word in set(words):
            node = self.suffixTree
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = True
            # print(word,self.suffixTree)
        self.queries = []
        # print(self.suffixTree)
            
        # print(self.letters)
        return 

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        node = self.suffixTree
        # word = self.queries[::]
        # # print(''.join(self.queries))
        # while len(word)>0:
        #     ch = word.pop()
        for ch in self.queries[::-1]:
            # print(ch)
            if '$' in node:
                return True
            if not ch in node:
                return False
            else:
                node = node[ch]
            
        # print(letter,''.join(self.queries),node,'$' in node)
        return '$' in node
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

