class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        dic = {}
        for i in range(1, m + 1):
            dic[i] = i - 1
        ans = []
        leng = 0
        for query in queries:
            index = dic[query]
            ans.append(index)

            for k, v in list(dic.items()):

                if v < index:
                    dic[k] += 1
                    leng += 1

            dic[query] = 0
        return ans
