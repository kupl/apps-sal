class Solution:
    def sortString(self, s: str) -> str:
        l = list(s)
        ope = list(s)
        s = ''
        while(ope):
            temp = []
            i = 0
            temp2 = list(set(ope))
            print('ji')
            while(ope and (ope) and temp2):
                n = min(temp2)

                if n not in temp:
                    temp.append(n)
                    ope.remove(n)
                    temp2.remove(n)
                print(temp)
                print((i, len(ope)))
                print(temp2)

                i += 1
            s += ''.join(temp)
            temp = []
            i = 0
            temp2 = list(set(ope))
            while(ope and len(ope) and temp2):
                n = max(temp2)
                if n not in temp:
                    temp.append(n)
                    ope.remove(n)
                    temp2.remove(n)
                i += 1
            s += ''.join(temp)

        return s
