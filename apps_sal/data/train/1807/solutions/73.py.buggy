class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        temp_lst = []
        temp=\"\"
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j//i <1 and j/i not in temp_lst:
                    temp_lst.append(j/i)
                    #print(temp_lst)
                    temp = str(j)+\"/\"+str(i)
                    ans.append(temp)
        return ans
