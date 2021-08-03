class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = self.convert_to_dic(A)
        for i in dic:
            if dic[i] > 1:
                return i

    def convert_to_dic(self, A):
        dic = {}
        for i in A:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return dic
