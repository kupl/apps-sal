class Solution:
     def shoppingOffers(self, rps,sos,tq):
         if len(sos)<1: return sum([x*y for x,y in zip(rps,tq)])
         so=sos.pop()
         m=self.shoppingOffers(rps,sos,tq)
         ss=so[:]
         while all([x<=y for x,y in zip(ss,tq)]):
             rq=[x-y for x,y in zip(tq,ss)]
             m=min(m,ss[-1]+self.shoppingOffers(rps,sos,rq))
             ss=[x+y for x,y in zip(ss,so)]
         sos.append(so)
         return m
