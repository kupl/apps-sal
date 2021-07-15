class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return self.solve(start, n)
    def solve(self, num, length):
        if length==1:
            if num==1:
                return [1, 0]
            return [0, 1]
        firstnum=1
        if num<2**(length-1):
            firstnum=0
        res=self.solve(num-firstnum*2**(length-1), length-1)
        ans=[]
        for i in res:
            ans.append(firstnum*2**(length-1)+i)
        res.reverse()
        for i in res:
            ans.append((1-firstnum)*2**(length-1)+i)
        return ans
