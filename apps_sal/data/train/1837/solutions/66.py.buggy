class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = {}
        tables = {}
        nos = set()
        for order in orders:
            nos.add(order[1])
            foods[order[2]] = 0
            
        for order in orders:
            if order[1] not in tables:
                tables[order[1]] = foods.copy()
            tables[order[1]][order[2]] += 1
        titles = [\"Table\"]
        foodkeys = sorted(foods.keys())
        for key in foodkeys:
            titles.append(key)
            
        nos = list(nos)
        nos = list(map(int,nos))
        nos = sorted(nos)
        print(nos)
        ans = []
        ans.append(titles)
        for i in nos:
            tmp = [str(i)]
            
            for key in foodkeys:
                tmp.append(str(tables[str(i)][key]))
            ans.append(tmp)
            
        return ans
        
        
            
