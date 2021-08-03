class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        order = {}
        uniquefood = set()
        for o in orders:
            tableno = o[1]
            item = o[2]
            uniquefood.add(item)
            if tableno not in order:
                order[tableno] = {item:1}
            else:
                if item not in order[tableno]:
                    order[tableno][item] = 1
                else:
                    order[tableno][item] += 1
        header = [\"Table\"]
        for i in sorted(uniquefood):
            header.append(i)
        res = [header]
        for o in sorted(order, key = lambda x:int(x)):
            temp = []
            temp.append(o)
            for i in header[1:]:
                if i in order[o]:
                    temp.append(str(order[o][i]))
                else:
                    temp.append(\"0\")
            res.append(temp)
        return res
        
