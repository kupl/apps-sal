class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food=[]
        d=OrderedDict()
        for _,_,k in orders:
            if k not in food:
                food.append(k)
        food.sort()
        n=len(food)
        new=[(i,f) for i,f in enumerate(food)]
        for _,j,k in orders:
            if j not in d:
                d[j]=[0 for _ in range(n)]
                for i,f in new:
                    if k==f:
                        d[j][i]=1
                        break               
            else:
                for i,f in new:
                    if k==f:
                        d[j][i]+=1
                        break
        d=OrderedDict(sorted(d.items(),key=lambda x:int(x[0])))
        title=['Table']+food
        details=[[k]+[str(i) for i in v] for k,v in d.items()]
        details.insert(0,title)
        return details
