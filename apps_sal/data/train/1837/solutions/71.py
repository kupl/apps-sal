class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = dict()
        food_items = set()
        
        for _, table, food in orders:
            table = int(table)
            if table not in d:
                d[table] = collections.Counter()
            d[table][food] += 1
            food_items.add(food)
        
        food_items = sorted(food_items)
        cols = ['Table'] + food_items
        
        
        out = [cols]
        for table in sorted(d.keys()):
            
            l = [str(table)]
            for f in food_items:
                if f not in d[table]:
                    l.append(\"0\")
                else:
                    l.append(str(d[table][f]))
            out.append(l)
        return out
                
        
        
        
            
            
            
        
        
        
