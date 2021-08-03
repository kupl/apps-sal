from collections import deque, defaultdict


class StreamChecker:

    def __init__(self, words: List[str]):
        # self.words = words
        # self.stream = deque(maxlen=2000)
        self.stream = deque(maxlen=2000)

        # organize based on last letter
        self.words_dict = defaultdict(list)
        for word in words:
            self.words_dict[word[-1]].append(word)

    def query(self, letter: str) -> bool:

        self.stream.append(letter)

        # for word in self.words:
        for word in self.words_dict[letter]:
            if len(word) <= len(self.stream):
                for i in range(len(word)):
                    if word[-(i + 1)] != self.stream[-(i + 1)]:
                        break
                else:
                    return True
                # if word == ''.join(self.stream[-len(word):]):
                #     return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
