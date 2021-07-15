from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        #having a dictionary of dictionaries?
        #should have a set of all the items?
        #ex: {2:{ceviche: 1}, {burrito: 2}, 3: {ceviche: 0}}
        
        items = set()
        tableorders = defaultdict(lambda: {})
        
        for i in orders:
            table = int(i[1])
            if tableorders[table] == {}:
                tableorders[table] = defaultdict(lambda: 0)
                tableorders[table][i[2]] += 1
                items.add(i[2])
            else:
                tableorders[table][i[2]] += 1
                items.add(i[2])
    
        items = sorted(items)
        chartorders = []
        column1 = [\"Table\"]
        for i in items:
            column1.append(i)
        chartorders.append(column1)
        for c in sorted(tableorders.keys()):
            tablerow = []
            tablerow.append(str(c))
            for z in items:
                if z in tableorders[c].keys():
                    tablerow.append(str(tableorders[c][z]))
                else:
                    tablerow.append(str(0))
            chartorders.append(tablerow)
        return chartorders
        
                    
