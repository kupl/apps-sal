class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)

        invalid = []
        hashtime = {}
        hashcity = {}
        hashindex = {}

        for i in range(n):
            t = transactions[i].split(',')
            n = t[0]
            ti = int(t[1])
            a = int(t[2])
            c = t[3]

            if hashtime.get(n) is None:
                hashtime[n] = [ti]
                hashcity[n] = [c]
                hashindex[n] = [i]

            else:
                for h in range(len(hashindex[n])):
                    li = hashtime[n][h]
                    lc = hashcity[n][h]
                    in1 = hashindex[n][h]
                    if abs(li - ti) <= 60 and not lc == c:
                        if transactions[in1] not in invalid:
                            invalid.append(transactions[in1])
                        if transactions[i] not in invalid:
                            invalid.append(transactions[i])

            if a > 1000:
                if transactions[i] not in invalid:
                    invalid.append(transactions[i])

            hashtime[n].append(ti)
            hashcity[n].append(c)
            hashindex[n].append(i)

            # print(invalid, t)

        return invalid
