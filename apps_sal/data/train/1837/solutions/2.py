from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        record = defaultdict(lambda: defaultdict(int))
        for _, table, item in orders:
            record[table][item] += 1
        
        res = []
        items = sorted(set(i for v in list(record.values()) for i in list(v.keys())))
        
        for table, v in list(record.items()):
            res.append([table] + ['0' if i not in v else str(v[i]) for i in items])
        
        res.sort(key=lambda x: [int(i) for i in x])
        res = [['Table'] + items] + res
        return res

