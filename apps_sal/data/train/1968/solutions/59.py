class Solution:
    class TrieNode:
        def __init__(self):
            self.lookup = {}
            self.word = False

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()

        def addPath(self, word):
            currNode = self.root
            for char in word:
                if char not in currNode.lookup:
                    currNode.lookup[char] = Solution.TrieNode()
                currNode = currNode.lookup[char]
            currNode.word = True

        def shortPath(self, word):
            currNode = self.root
            for index, char in enumerate(word):
                if currNode.word and char == '/':
                    return word[:index]
                currNode = currNode.lookup[char]

            return word

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Solution.Trie()
        result = set()
        for path in folder:
            trie.addPath(path)

        for path in folder:
            result.add(trie.shortPath(path))

        return list(result)
