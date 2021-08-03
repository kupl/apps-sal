class StreamChecker:

    def __init__(self, words: List[str]):

        self.curr = ''
        self.words = words
        temp = []
        for w in words:
            temp.append(w[-1])
        self.last = temp

        self.MAX = 1
        self.lenth = []
        self.storage = collections.defaultdict(list)
        for w in words:
            if len(w) not in self.lenth:
                self.lenth.append(len(w))
            self.storage[len(w)].append(w)
            self.MAX = max(self.MAX, len(w))

    def query(self, letter: str) -> bool:

        # print('start', letter, self.curr)

        if len(self.curr) < self.MAX:
            self.curr += letter
        elif len(self.curr) == self.MAX:
            self.curr = self.curr[1:] + letter

        # print(letter, self.curr)

        if letter in self.last:

            # print('in')

            for i in range(1, len(self.curr) + 1):
                # print(i, self.curr, self.curr[-i:])
                if self.curr[-i:] in self.storage[i]:
                    return True
                else:
                    continue
            return False

        else:
            return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
