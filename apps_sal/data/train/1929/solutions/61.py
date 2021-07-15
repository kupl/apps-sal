class StreamChecker:

    def __init__(self, words: List[str]):
        self.d = {}
        for w in words:
            tmp = self.d
            for i in w:
                tmp = tmp.setdefault(i, {})
            tmp['#'] = {}
        self.cur = []
    # def merge(self, d1, d2):
    #     res = {}
    #     for k in set(list(d1.keys()) + list(d2.keys())):
    #         if k in d1 and k in d2:
    #             res[k] = self.merge(d1[k], d2[k])
    #         elif k in d1:
    #             res[k] = d1[k]
    #         else:
    #             res[k] = d2[k]
    #     return res

    def query(self, letter: str) -> bool:
        flag = False
        cur_new = []
        for prefix in self.cur:
            if letter in prefix:
                cur_new.append(prefix[letter])
                if \"#\" in prefix[letter]:
                    flag = True
        if letter in self.d:
            cur_new.append(self.d[letter])
            if \"#\" in self.d[letter]:
                flag = True
        self.cur = cur_new
        return flag

        # flag = False
        # tmp = {}
        # if letter in self.cur:
        #     tmp = self.cur[letter]
        #     if ('#' in tmp):
        #         flag = True
        #         tmp.pop('#')
        # self.cur = self.merge(tmp, self.d)
        # return flag
         
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
