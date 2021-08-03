class Solution:
    def sortString(self, s: str) -> str:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        self.d = d
        self.re = ''

        print((self.d))
        while True:
            if self.d == {}:
                break
            smallest = min(self.d)

            if smallest:
                self.re += smallest
                if self.d[smallest] == 1:
                    del self.d[smallest]
                else:
                    self.d[smallest] -= 1
            else:
                break

            while True:
                nexts = None
                for key in self.d:
                    if key > smallest:
                        if nexts is None:
                            nexts = key
                        else:
                            nexts = min(key, nexts)
                if nexts:
                    if self.d[nexts] == 1:
                        del self.d[nexts]
                    else:
                        self.d[nexts] -= 1
                    self.re += nexts
                else:
                    break
                smallest = nexts

            if self.d == {}:
                break

            biggest = max(self.d)

            if biggest:
                self.re += biggest
                if self.d[biggest] == 1:
                    del self.d[biggest]
                else:
                    self.d[biggest] -= 1
            else:
                break

            while True:
                nexts = None
                for key in self.d:
                    if key < biggest:
                        if nexts is None:
                            nexts = key
                        else:
                            nexts = max(key, nexts)
                if nexts:
                    if self.d[nexts] == 1:
                        del self.d[nexts]
                    else:
                        self.d[nexts] -= 1
                    self.re += nexts
                else:
                    break
                biggest = nexts

        print((self.d))
        return self.re
