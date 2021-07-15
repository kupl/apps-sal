from collections import defaultdict
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root={'*':'*'}
        for word in words:
            curr_node=self.root
            for letter in word:
                if letter not in curr_node:
                    curr_node[letter]={}
                curr_node=curr_node[letter]
            curr_node[\"*\"]=\"*\"
        self.stream=[]

    def query(self, letter: str) -> bool:
        temp=[]
        self.stream.append(self.root)
        for i in self.stream:
            if letter in i:
                temp.append(i[letter])
        self.stream=temp
        for i in self.stream:
            if \"*\" in i:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
