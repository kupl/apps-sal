class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @lru_cache(maxsize=None)
        def minmax(st, m, player):
            if(st >= len(piles)):
                return 0
            if(player):
                return max([sum(piles[st:st + x]) + minmax(st + x, max(x, m), player ^ 1) for x in range(1, 2 * m + 1)])
            else:
                return min([minmax(st + x, max(m, x), player ^ 1) for x in range(1, 2 * m + 1)])

        return minmax(0, 1, 1)


#         piles=[0]+piles

#         self.p1=float('inf')
#         def traverse(piles,ind,ch,m,p1,p2):
#             print(ind,p1,p2)
#             if(ind==len(piles)):
#                 self.p1=min(p1,self.p1)
#             if(ch==1):
#                 su=0
#                 for i in range(ind,min(ind+2*m+1,len(piles))):
#                     su+=piles[i]
#                     traverse(piles,i+1,ch^1,max(m,i),p1+su,p2)

#             else:
#                 su=0
#                 for i in range(ind,min(ind+2*m+1,len(piles))):
#                     su+=piles[i]
#                     traverse(piles,i+1,ch^1,max(m,i),p1,p2+su)

#         traverse(piles,1,1,1,0,0)

#         return self.p1
