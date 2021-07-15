class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        mytables = set()
        
        header = set(\" \")
        mytablefood = collections.Counter()
        
        for customerName, table, food in orders:
            header.add(food)
            mytables.add(table)
            mytablefood[table+food] += 1
        
        header = list(header)
        header.sort()
        header[0] = \"Table\"
        output = [header]
        
        mytables = sorted(mytables, key=int)
        for table in mytables:
            T = [table]
            for food in header[1:]:
                T.append(str(mytablefood[table+food]))
            output.append(T)
        return output
