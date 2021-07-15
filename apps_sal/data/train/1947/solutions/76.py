class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        A_dict = []
        B_dict = {} #final dictionary of B taking max of cnt
        ans = []
        for ww in A:
            temp = {}
            for ele in ww:
                if ele in temp:
                    temp[ele] +=1
                else:
                    temp[ele] =1
            A_dict.append(temp)
        for ww in B:
            temp = {}
            for ele in ww:
                if ele in temp:
                    temp[ele] +=1
                else:
                    temp[ele] =1
            for key,cnt in temp.items():
                if key in B_dict:
                    B_dict[key] = max(cnt,B_dict[key])
                else:
                    B_dict[key] = cnt
        for ind,ele in enumerate(A_dict):
            cur_dict = ele
            flag = True
            for key,cnt in B_dict.items():
                if key not in cur_dict or cur_dict[key]<cnt:
                    flag = False
                    break
            if flag:
                ans.append(A[ind])
        return ans
