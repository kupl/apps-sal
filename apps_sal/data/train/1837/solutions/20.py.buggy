class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dishes = list({order[2] for order in orders})
        dishes.sort()
        res=[[\"Table\"]]
        res[0].extend(dishes)
        hashmap=defaultdict(dict)
        for order in orders:
            if order[2] in hashmap[order[1]]:
                hashmap[order[1]][order[2]]+=1
            else:
                hashmap[order[1]][order[2]]=1
        cust = sorted({int(c[1]) for c in orders})
        for cus in cust:
            cus=str(cus)
            alist = []
            order = hashmap[cus]
            for dish in dishes:
                if dish in order:
                    alist.append(str(order[dish]))
                else:
                    alist.append(\"0\")
            alist=[cus] + alist
            res.append(alist)
        return res

