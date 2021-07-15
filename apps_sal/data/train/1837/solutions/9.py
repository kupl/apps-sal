class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dishes = list({order[2] for order in orders})
        dishes.sort()
        res = [[\"Table\"]]
        res[0].extend(dishes)
        hashmap = collections.defaultdict(dict)
        for o in orders:
            if o[2] in hashmap[o[1]]:
                hashmap[o[1]][o[2]] += 1
            else:
                hashmap[o[1]][o[2]] = 1
        
        cust = sorted({int(c[1]) for c in orders})
        for c in cust:
            no = str(c)
            lst = []
            order = hashmap[no]
            for od in dishes:
                if od in order:
                    lst.append(str(order[od]))
                else:
                    lst.append(\"0\")
            lst = [no] + lst
            res.append(lst)
        return res
        
