class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dic = {}
        result = []
        for i, s in enumerate(transactions):
            [n,m,a,c] = s.split(\",\")
            if int(a)>1000:
                result.append(s)
            if n not in dic:
                dic[n] = [[m,c,i]]
            else:
                dic[n].append([m,c,i])
                for ml, cl, ii in dic[n]:
                    if cl!=c:
                        if abs(int(ml)-int(m))<=60:
                            if s not in result: result.append(s)
                            if transactions[ii] not in result: result.append(transactions[ii])
            # print(dic)
        return result
