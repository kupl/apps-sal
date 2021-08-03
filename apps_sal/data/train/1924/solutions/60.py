class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        temp = []
        for t in transactions:
            temp.append(t.split(','))

        res = []
        for i in range(len(temp)):
            if int(temp[i][2]) > 1000 and ','.join(temp[i]) not in res:
                res.append(','.join(temp[i]))
            for j in range(i + 1, len(temp)):
                if temp[i][0] == temp[j][0] and temp[i][3] != temp[j][3]:
                    if abs(int(temp[i][1]) - int(temp[j][1])) <= 60:
                        if ','.join(temp[i]) not in res:
                            res.append(','.join(temp[i]))
                        if ','.join(temp[j]) not in res:
                            res.append(','.join(temp[j]))
        return res
