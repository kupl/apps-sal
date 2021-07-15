class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_idxes = set()
        dct = {}
        tracs = []
        for idx, trc in enumerate(transactions):
            name, time, amount, location = trc.split(\",\")
            time = int(time)
            amount = int(amount)
            tracs.append((name, time, location, idx, amount))
        # print(sorted(tracs))
            
        for name, time, location, idx, amount in tracs:
            # if name == 'lee' and time == 152:
            #     print(name, time, location, idx, amount )
            #     print(dct['lee'])
            if amount > 1000:
                invalid_idxes.add(idx)
                # continue
            for prev_name, prev_time, prev_location, prev_idx, _ in tracs:
                # prev_idx, prev_time, prev_location = dct[name]
                if prev_name == name and abs(time - prev_time) <= 60 and prev_location != location:
                    invalid_idxes.add(idx)
                    invalid_idxes.add(prev_idx)
            # dct[name] = (idx, time, location)
            
        return [transactions[idx] for idx in invalid_idxes]
            
