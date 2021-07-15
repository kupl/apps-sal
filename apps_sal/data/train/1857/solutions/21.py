class Solution:
    def maxNumberOfFamilies(self, n: int, r: List[List[int]]) -> int:
        r=sorted(r)
        l=[0 for i in range(10)]
        ans=0
        n_occ=0
        r.append([0,0])
        for i in range(0,len(r)):
            if i==0:
                l[r[0][1]-1]=1
            else:
                if r[i][0]==r[i-1][0]:
                    l[r[i][1]-1]=1
                else:
                    n_occ+=1
                    if (l[1]==0)&(l[2]==0)&(l[3]==0)&(l[4]==0):
                        ans+=1
                        if (l[5]==0)&(l[6]==0)&(l[7]==0)&(l[8]==0):
                            ans+=1
                    elif (l[5]==0)&(l[6]==0)&(l[7]==0)&(l[8]==0):
                        ans+=1
                    elif (l[3]==0)&(l[4]==0)&(l[5]==0)&(l[6]==0):
                        ans+=1
                    #print(r[i],l)
                    l=[0 for i in range(10)]   
                    l[r[i][1]-1]=1
        ans+=(n-n_occ)*2
        return ans
