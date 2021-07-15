class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        def get_bit(word):
            x=0
            for ch in (word):
                x|=1<<(ord(ch)-ord('a'))
            return x
        bitdic=collections.defaultdict(int)
        words=[set(list(x)) for x in words]
        for word in words:
            bitdic[get_bit(word)]+=1
        res=[]
        for puzzle in puzzles:
            count=0
            first=puzzle[0]
            bfs=[1<<(ord(first)-ord('a'))]
            for ch in set(puzzle[1:]):
                bfs+=[x|1<<(ord(ch)-ord('a')) for x in bfs]
            res.append(sum(bitdic[x] for x in set(bfs)))
        return res

