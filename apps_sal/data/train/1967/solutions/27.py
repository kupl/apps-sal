class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        b = []
        c = []
        def additivenumber(num,b):
            if len(c) == 1:
                return \"\"
            if len(b) > 2 and num == \"\":
                c.append(b)
            else:
                for x in range(len(num)):
                    if len(num[0:x+1]) == 1:
                        if len(b) >= 2:
                            if int(num[0:x+1]) == b[-1] + b[-2]:
                                additivenumber(num[x+1:],b+[int(num[0:x+1])])
                        else:
                            additivenumber(num[x+1:],b+[int(num[0:x+1])])
                    else:
                        if num[0:x+1][0] != str(0) and int(num[0:x+1]) <= 2147483647:
                            if len(b) >= 2:
                                if int(num[0:x+1]) == b[-1] + b[-2]:
                                    additivenumber(num[x+1:],b+[int(num[0:x+1])])
                            else:
                                additivenumber(num[x+1:],b+[int(num[0:x+1])])
        additivenumber(num,b)
        if c == []:
            return c
        return c[0]
        
