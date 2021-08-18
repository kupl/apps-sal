class StreamChecker:

    def __init__(self, words: List[str]):
        self.dict_tree = {}
        for i in words:
            cur = self.dict_tree
            for j in i:
                if j not in cur:
                    cur[j] = {}
                cur = cur[j]
            cur[-1] = True
        self.char_stream = []
        self.to_check = []

    def query(self, letter: str) -> bool:
        temp = []
        find = False
        for i in self.to_check:
            if letter in i:
                i = i[letter]
                temp.append(i)
                if -1 in i:
                    find = True
        if letter in self.dict_tree:
            if -1 in self.dict_tree[letter]:
                find = True
            temp.append(self.dict_tree[letter])
        self.to_check = temp
        return True if find else False
