class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        items_all = sorted(list(set([ele[2] for ele in orders])))
        tb_disp = {}
        for od in orders:
            tbn = od[1]
            itm = od[2]
            if tbn not in tb_disp:
                tb_disp[tbn] = [0 for _ in range(len(items_all))]
            tb_disp[tbn][items_all.index(itm)] +=1
        ans_li = sorted([[tb,itm] for tb,itm in tb_disp.items()],key=lambda x:int(x[0]))
        ans = [[\"Table\"]+items_all]
        for ele in ans_li:
            temp = [str(ele[0])]
            for it in ele[1]:
                temp.append(str(it))
            ans.append(temp)
        return ans
            
        
        
                
