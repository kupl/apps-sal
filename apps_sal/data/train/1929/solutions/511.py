class StreamChecker:
    from collections import deque

    def __init__(self, words: List[str]):
        self.max = len(max(words, key=len))
        self.words = tuple(words)
        self.letters = deque(maxlen=self.max)

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        l = ''.join(self.letters)
        return l.endswith(self.words)
    "\n    def __init__(self, words: List[str]):\n        self.words = set(words)\n        self.letters = ''\n        self.fragments = {}\n        for w in words:\n            temp = self.fragments\n            for i in range(len(w)):\n                sec = w[len(w)-1-i:]\n                if sec not in temp:\n                    temp[sec] = {}\n                temp = temp[sec]\n                    \n    def query(self, letter: str) -> bool:\n        self.letters += letter\n        chars = self.letters\n        \n        temp = self.fragments\n        for i in range(len(chars)):\n            sec = chars[len(chars) - 1 - i:]\n            if sec in self.words:\n                return True\n            if sec not in temp:\n                return False\n            temp = temp[sec]\n    "
    "\n    def __init__(self, words: List[str]):\n        self.words = tuple(words)\n        self.letters = ''\n        \n    def query(self, letter: str) -> bool:\n        self.letters +=letter\n        return self.letters.endswith(self.words)        \n    "
