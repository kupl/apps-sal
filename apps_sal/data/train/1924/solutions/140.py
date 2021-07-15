class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        data_by_time = {}
        for data in transactions:
            orig_data = data
            data = data.split(\",\")

            transaction = {\"name\": data[0], \"amount\": int(data[2]), \"city\": data[3], \"orig\": orig_data}
            if int(data[1]) not in data_by_time:
                data_by_time[int(data[1])] = [transaction]
            else:
                data_by_time[int(data[1])].append(transaction)
        result = set()
        times = sorted(data_by_time.keys())
        for time in times:
            for trans in data_by_time[time]:
                if trans[\"amount\"] > 1000:
                    result.add(trans[\"orig\"])
    
        for (t_trans, trans_list) in data_by_time.items():
            for trans in trans_list:
                for time in times:
                    if abs(t_trans - time) <= 60:
                        for other_trans in data_by_time[time]:
                            if other_trans[\"name\"] == trans[\"name\"] and other_trans[\"city\"] != trans[\"city\"]:
                                result.add(other_trans[\"orig\"])
                                result.add(trans[\"orig\"])
                    
        #for i in range(len(times) - 1):
        #    if times[i+1] - times[i] <= 60:
        #        seen_names = {}
        #        for transaction in data_by_time[times[i]]:
        #            seen_names[transaction[\"name\"]] = transaction
        #        for transaction in data_by_time[times[i+1]]:
        #            if transaction[\"name\"] in seen_names:
        #                if transaction[\"city\"] != seen_names[transaction[\"name\"]][\"city\"]:
        #                    result.add(transaction[\"orig\"])
        #                    result.add(seen_names[transaction[\"name\"]][\"orig\"])
        #                    #result.update([seen_names[x][\"orig\"] for x in seen_names[transaction[\"name\"]]])
        return list(result)
                    
        
        
