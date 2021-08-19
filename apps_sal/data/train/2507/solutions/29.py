class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        r = 0
        a = list(chars)
        # print(a)
        for i in words:
            b = a.copy()
            s = False
            for j in i:
                if j not in b:
                    s = True
                else:
                    b.remove(j)

            if s != True:
                r += len(i)
                # print(s,r,b,a)
        return r
