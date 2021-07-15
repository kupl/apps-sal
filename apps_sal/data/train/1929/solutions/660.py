from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.wordsSet = Trie(words)
        self.letters = \"\"

    def query(self, letter: str) -> bool:
        self.letters += letter
        tmpLetterSequence = \"\"
        for i in range(len(self.letters)-1,-1,-1):
            tmpLetterSequence += self.letters[i]
            if not self.wordsSet.isPrefix(tmpLetterSequence):
                return False
            if self.wordsSet.hasWord(tmpLetterSequence):
                return True
        return False


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            tmpRoot = self.root
            for j in range(len(word) -1 , -1, -1):
                letter = word[j]
                if tmpRoot.children[ord(letter)-ord('a')] is None:
                    tmpRoot.children[ord(letter)-ord('a')] = Node()
                tmpRoot = tmpRoot.children[ord(letter)-ord('a')]
            tmpRoot.end = True

    def isPrefix(self, word):
        tmpRoot = self.root
        for letter in word:
            if tmpRoot.children[ord(letter) - ord('a')] is None:
                return False
            tmpRoot = tmpRoot.children[ord(letter) - ord('a')]
        return True

    def hasWord(self, word):
        tmpRoot = self.root
        for letter in word:
            if tmpRoot.children[ord(letter) - ord('a')] is None:
                return False
            tmpRoot = tmpRoot.children[ord(letter) - ord('a')]
        if tmpRoot.end:
            return True
        return False
