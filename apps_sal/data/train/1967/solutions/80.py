class Solution:
    def __init__(self):
        self.res = []
    
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def helper(pos, temp):
            if pos == len(S): 
                if len(temp) > 2:
                    self.res = temp[:]
                return 
            if S[pos] == '0':
                if len(temp) > 1:
                    if temp[-1] + temp[-2] != 0:
                        return
                temp.append(0)
                helper(pos + 1, temp)
                temp.pop()
            else:
                for i in range(pos + 1, len(S) + 1):
                    curr = int(S[pos : i])
                    if len(temp) < 2:
                        temp.append(curr)
                        helper(i, temp)
                        temp.pop()
                    else:
                        if curr > temp[-1] + temp[-2] or curr > 2 ** 31 - 1:
                            return
                        if curr == temp[-1] + temp[-2]:
                            temp.append(curr)
                            helper(i, temp)
                            temp.pop()
        helper(0, [])
        return self.res
