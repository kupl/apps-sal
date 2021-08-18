
class Tree:
    def __init__(self, val=''):
        self.val = val
        self.isTerminal = False
        self.subs = dict()


class StreamChecker:

    def __init__(self, words: List[str]):

        self.possibleNodes = list()
        self.root = Tree()

        for word in words:
            traverser = self.root
            for char in word:
                if char in traverser.subs:
                    traverser = traverser.subs[char]
                else:
                    node = Tree(char)
                    traverser.subs[char] = node
                    traverser = node
            traverser.isTerminal = True

    def query(self, letter: str) -> bool:

        newPossibleNodes = []
        if letter in self.root.subs:
            newPossibleNodes.append(self.root.subs[letter])

        for node in self.possibleNodes:
            if letter in node.subs:
                newPossibleNodes.append(node.subs[letter])

        self.possibleNodes = newPossibleNodes

        for node in newPossibleNodes:
            if node.isTerminal:
                return True

        return False
