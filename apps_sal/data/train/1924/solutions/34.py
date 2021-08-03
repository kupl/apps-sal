class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        seen = {}
        final = []

        for i in transactions:
            j = i.split(',')

            name = j[0]
            time = int(j[1])
            amount = int(j[2])
            city = j[3]

            if name not in seen:
                seen[name] = [[name, time, amount, city, i]]
            else:
                seen[name].append([name, time, amount, city, i])

        for key in list(seen.keys()):
            keys_by_time = {}
            # print(key,len(seen[key]))
            # print(seen[key])
            for i in range(len(seen[key])):
                # print(seen[key][i][1])
                keys_by_time[seen[key][i][1]] = i
            seen[key].append(keys_by_time)
            # print(seen[key])

        for key in list(seen.keys()):

            for i in range(len(seen[key]) - 1):

                for j in range(i + 1, len(seen[key]) - 1):

                    current = seen[key][i]
                    nex = seen[key][j]

                    # print(\"current \",current[1],\"nex \",nex[1])
                    if current[3] != nex[3] and abs(current[1] - nex[1]) <= 60:
                        # print(\"condition1\")
                        if current[4] not in final:
                            final.append(current[4])
                        if nex[4] not in final:
                            final.append(nex[4])

                if seen[key][i][4] not in final and seen[key][i][2] > 1000:
                    # print(\"condition2\")
                    final.append(seen[key][i][4])
        return final
