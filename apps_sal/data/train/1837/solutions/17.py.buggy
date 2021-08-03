class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food=[]
        t={}
        disp=[]
        for i in orders:
            food.append(i[2])
            if i[1] in t:
                t[i[1]].append(i[2])
            else:
                t[i[1]]=[]
                t[i[1]].append(i[2])
        tmp =[\"Table\"]
        food=sorted(set(food))
        tmp.extend(food)
        disp.append(tmp)

        for k in sorted(t.keys(), key=lambda i:int(i)):
            tmp=[]
            tmp.append(k)
            for f in food:
                foodct=0
                if f in t[k]:
                    foodct = t[k].count(f)
                tmp.append(str(foodct))
            disp.append(tmp)
        print(disp)
        return disp

