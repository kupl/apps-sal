class StreamChecker:
    def __init__(self, words: List[str]):
        self.d = [{}, False]
        for word in words:
            condition = self.d
            for letter in word:
                if letter not in condition[0]:
                    condition[0][letter] = [{}, False]
                condition = condition[0][letter]
            condition[1] = True
        self.pool = [self.d]
        # print(self.d)

    def query(self, letter: str) -> bool:
        new_pool = [self.d]
        ret = False
        for one in self.pool:
            if letter in one[0]:
                if one[0][letter][1]:
                    ret = True
                new_pool.append(one[0][letter])
        self.pool = new_pool
        # print(self.pool)

        return ret


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
