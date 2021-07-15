from collections import deque, defaultdict


class StreamChecker:

    def __init__(self, words: List[str]):
        words = sorted(words, key=len)
        self.words_by_len = defaultdict(set)
        for word in words:
            if all(word[-length:] not in words_set for length, words_set in list(self.words_by_len.items())):
                self.words_by_len[len(word)].add(word)
        
        self.search_history = deque(maxlen=max(self.words_by_len.keys()))

    def query(self, letter: str) -> bool:
        self.search_history.append(letter)
        history = ''.join(self.search_history)
        
        return any(history[-length:] in words_set for length, words_set in list(self.words_by_len.items()))
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

