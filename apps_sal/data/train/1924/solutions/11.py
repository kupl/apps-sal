class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed_ts = []
        invalid_ts = set()
        for t in transactions:
            t_list = t.split(',')
            # print(t_list)
            t_dict={}
            t_dict['str'] = t
            t_dict['name'] = t_list[0]
            t_dict['time'] = int(t_list[1])
            t_dict['amount'] = int(t_list[2])
            t_dict['city'] = t_list[3]
            
            if t_dict['amount']>1000:
                invalid_ts.add(t)
            for t2 in parsed_ts:
                if abs(t_dict['time']-t2['time'])<=60 and t_dict['city']!=t2['city'] and t_dict['name']==t2['name']:
                    invalid_ts.add(t_dict['str'])
                    invalid_ts.add(t2['str'])
            parsed_ts.append(t_dict)
        
        return list(invalid_ts)

