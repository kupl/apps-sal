
class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = {}
        for word in words:
            t = self.t
            for ch in word:
                t = t.setdefault(ch, {})
            t['#'] = 'END'

        self.cursors = [self.t]

    def query(self, letter: str) -> bool:

        newcursors = []
        ans = False

        for cur in self.cursors:
            if letter not in cur:
                continue
            cur = cur[letter]
            if '#' in cur:
                ans = True
            newcursors.append(cur)

        self.cursors = newcursors
        self.cursors.append(self.t)

        return ans


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
