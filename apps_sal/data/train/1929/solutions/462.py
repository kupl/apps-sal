class StreamChecker:
    def __init__(self,words:List[str]):
        self.s,self.dic='',collections.defaultdict(set)
        for i in words:self.dic[i[-1]].add(i)
    def query(self,letter:str)->bool:
        self.s+=letter
        return any(self.s.endswith(i) for i in self.dic[letter])
