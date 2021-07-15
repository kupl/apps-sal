class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d={}
        groups=[{2,3,4,5},{4,5,6,7},{6,7,8,9}]
        for x,y in reservedSeats:
            if(x in d):
                d[x].append(y)
            else:
                d[x]=[y]
        ans=0
        for v in d.keys():
            res=set(d[v])
            c=\"\"
            for g in groups:
                if(not(g&res)):
                    c+=\"1\"
                else:
                    c+=\"0\"
            if(int(c,2)==0):
                ans+=0
            elif(int(c,2)==5 or int(c,2)==7):
                ans+=2
            else:
                ans+=1
        return ans+2*(n-len(d))
    
