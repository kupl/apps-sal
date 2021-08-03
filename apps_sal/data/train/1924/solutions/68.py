class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        invalid_check = [0] * n
        for i in range(n):
            i_info = transactions[i].split(',')
            assert(len(i_info) == 4)
            if(int(i_info[2]) >= 1000):
                invalid_check[i] = 1
            for j in range(i + 1, n):
                j_info = transactions[j].split(',')
                assert(len(j_info) == 4)
                if(i_info[0] == j_info[0]
                   and i_info[3] != j_info[3]
                        and abs(int(i_info[1]) - int(j_info[1])) <=60) :
                    invalid_check[i] = invalid_check[j] = 1
        ret = []
        for i in range(n):
            if(invalid_check[i]):
                ret.append(transactions[i])
        return ret
