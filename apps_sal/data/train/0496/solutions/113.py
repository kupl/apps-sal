class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        dic = dict(collections.Counter(A))
        sortedDic = sorted(list(dic.items()), key=lambda x: x[0])

        result = 0

        while sortedDic:
            num, freq = sortedDic.pop(0)
            if freq > 1:
                diff = freq - 1

                if sortedDic and sortedDic[0][0] == num + 1:
                    sortedDic[0] = (num + 1, diff + sortedDic[0][1])
                else:
                    sortedDic.insert(0, (num + 1, diff))

                result += diff

        return result
