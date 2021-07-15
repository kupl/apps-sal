class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        head = self.trie
        self.history = \"\"
        
        for w in words:
            p = head
            for i in range(len(w)-1, -1, -1):
                if i==0:
                    if w[i] not in p:
                        p[w[i]] = {'#' : True}
                    else:
                        p[w[i]]['#'] = True
                else:
                    if w[i] not in p:
                        p[w[i]] = {'#' : False}
                        p = p[w[i]]
                    else:
                        p = p[w[i]]
        print(self.trie)
                    

    def query(self, letter: str) -> bool:
        self.history += letter
        # print(self.history)
        head = self.trie
        for i in self.history[::-1]:
            # print(i)
            if i in head:
                if head[i]['#']==True:
                    return True
                else:
                    head =  head[i]
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
