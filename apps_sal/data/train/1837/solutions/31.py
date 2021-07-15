class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = OrderedDict()
        
        for k in orders:
            if k[1] not in table:
                table[k[1]]={}
            
            if k[2] in table[k[1]]:
                table[k[1]][k[2]] += 1
            else:
                table[k[1]][k[2]] = 1
        
        d_order = sorted([int(i) for i in table.keys()])
        
        d_order = [str(i) for i in d_order]
        
        f_order = sorted(set([k[2] for k in orders]))
        
        print(d_order, f_order)
        print(table)
        res = []
        
        res.append([\"Table\"] + f_order)
        
        for k in d_order:
            tmp = [k]
            for _k in f_order:
                if _k in table[k]:
                    tmp.append(str(table[k][_k]))
                else:
                    tmp.append(\"0\")
            res.append(tmp)
        return res

            
            
