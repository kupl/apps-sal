class Node:
    def __init__(self):
        self.isEnd = False
        self.next = {}
    def __repr__(self):
        return str(self.next)
        

class StreamChecker:

    def __init__(self, words: List[str]):
        self.dic = {}        
        for word in words:
            self.add(self.dic, word[::-1])
        print(self.dic)
        self.validLetters = \"\"
        
    def add(self, dic, word):
        currentLetter = word[0]
        if currentLetter not in dic.keys():
            dic[currentLetter] = Node()
        if len(word) != 1:
            self.add(dic[currentLetter].next, word[1:])
        else:
            dic[currentLetter].isEnd = True
            
    def __partial_query(self, dic, word):
        currentLetter = word[0]
        if currentLetter not in dic.keys():
            return False
        else:
            if dic[currentLetter].isEnd:
                return True
            else:
                if len(word) != 1:
                    return self.__partial_query(dic[currentLetter].next, word[1:])
                else:
                    return False
            
    def partial_query(self, word):
        return self.__partial_query(self.dic, word)
        

    def query(self, letter: str) -> bool:
        self.validLetters = letter + self.validLetters
        return self.partial_query(self.validLetters)
                

        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
