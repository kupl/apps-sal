import collections
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic=Counter(A)
        for i in dic:
            if(dic[i]>1):
                return i
        # dic={}
        # if(len(A)>0):
        #     for i in A:
        #         if i in dic:
        #             return i
        #         else:
        #             dic[i]=1

