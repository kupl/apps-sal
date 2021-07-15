class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        remove_ls = []
        start = True
        tmp = S
        while start or tmp != S:
            start = False
            tmp = S
            i = 0
            while i < len(S) - 1:
                if S[i] == S[i+1]:
                    if i + 2:
                        S = S[:i] + S[i+2 :]
                    else:
                        S = S[:i]
                i += 1
            if tmp == S:
                break
            
        # print(S)
        return S
        
        # return res
        # print(remove_ls)
        
        
#         remove_ls = []
#         for i in range(len(S) - 1):
#             if S[i] == S[i + 1]:
#                 if i not in remove_ls:
#                     remove_ls.append(i)
#                 remove_ls.append(i + 1) 

#             if remove_ls == []:
#                 break

#         res = \"\"
#         for i in range(len(S)):
#             if i not in remove_ls:
#                 res += S[i]
#         S = res    
#         start = False

