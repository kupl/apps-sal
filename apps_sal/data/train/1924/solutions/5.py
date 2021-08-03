import collections


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        def parse(S):
            fields = S.split(',')
            return [fields[0], int(fields[1]), int(fields[2]), fields[3]]

        hashMap = defaultdict(list)
        for S in transactions:
            fields = parse(S)
            hashMap[fields[0]].append(fields[1:])

        invalid = set([])
        for key in hashMap:
            vals = hashMap[key]

            for i, val1 in enumerate(vals):
                if val1[1] >= 1000:
                    invalid = invalid.union(set([','.join([key, str(val1[0]), str(val1[1]), val1[2]])]))
                if len(vals) <= 1:
                    continue
                for j, val2 in enumerate(vals[i + 1:]):
                    if abs(val1[0] - val2[0]) <= 60 and val1[2] != val2[2]:
                        invalid = invalid.union(set([','.join([key, str(val1[0]), str(val1[1]), val1[2]])]))
                        invalid = invalid.union(set([','.join([key, str(val2[0]), str(val2[1]), val2[2]])]))

        return list(invalid)
