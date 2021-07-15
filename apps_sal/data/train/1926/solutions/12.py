class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        l1,r1 = self.cldv(num+1)
        l2,r2 = self.cldv(num+2)
        d1=r1-l1
        d2=r2-l2
        if d1<d2:
            return [l1,r1]
        else:
            return [l2,r2]

    def cldv(self, n):
        s = int(n**0.5)
        while n%s!=0:
            s-=1
        return s,n//s
