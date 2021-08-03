class StreamChecker:

    def __init__(self, words: List[str]):
        self.h = {}
        for word in words:
            curr_node = self.h           
            for x in range(len(word)):
                curr = word[x]
                if curr not in curr_node: curr_node[curr] = {}
                curr_node = curr_node[curr]
            curr_node[\"#\"] = True
        self.nodes = []

        
    def query(self, letter: str) -> bool:
        result = False
        self.nodes.append(self.h)
        new = []
        for node in self.nodes:
            if letter in node:
                node = node[letter]
                if \"#\" in node: result = True
                new.append(node)
        self.nodes = new     
        return result


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
