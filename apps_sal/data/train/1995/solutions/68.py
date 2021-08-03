class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans_dic = [0] * 1000
        for i in trips:
            for j in range(i[1], i[2]):
                if ans_dic[j]:
                    ans_dic[j] += i[0]
                    if ans_dic[j] > capacity:
                        return False
                else:
                    ans_dic[j] = i[0]
        # print(ans_dic)
        return True
