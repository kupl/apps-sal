class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # 1)
        i, A2, seen = 0, [], set()
        while i < len(A):
            if A[i] not in seen:
                seen.add(A[i])
                dct = {}
                for char in A[i]:
                    if char in dct:
                        dct[char] += 1
                    else:
                        dct[char] = 1
                A2.append(dct)
                i += 1
            else:
                A.pop(i)
                
        i, seen = 0, set()
        while i < len(B):
            if B[i] not in seen:
                seen.add(B[i])
                dct = {}
                for char in B[i]:
                    if char in dct:
                        dct[char] += 1
                    else:
                        dct[char] = 1
                B[i] = dct
                i += 1
            else:
                B.pop(i)
        
        # 2) merge all the dicts of B into one dict
        while len(B) > 1:
            for key in B[1]:
                if key in B[0]:
                    B[1][key] = max(B[1][key], B[0][key])
            for key in B[0]:
                if key not in B[1]:
                    B[1][key] = B[0][key]
            B.pop(0)
        B_dct = B[0]
        
        # 3)
        ans, A_len, B_len = [], len(A), len(B)
        for i in range(A_len):
            isSubset = True
            for key in B_dct:
                if key not in A2[i] or (key in A2[i] and B_dct[key] > A2[i][key]):
                    isSubset = False
                    break
            if isSubset:
                ans.append(A[i])
        return ans
