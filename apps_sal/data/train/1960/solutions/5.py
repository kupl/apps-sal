class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        P_lst = [i for i in range(1, m + 1)]
        q_list = []
        for i in range(0, len(queries)):
            target = queries[i]
            for j in range(0, len(P_lst)):

                if P_lst[j] == target:
                    q_list.append(j)
                    x = P_lst.pop(j)
                    P_lst.insert(0, x)
                    break
        return q_list
