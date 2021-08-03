class Solution:
    def splitIntoFibonacci(self, S):
        \"\"\"
        :type S: str
        :rtype: List[int]
        \"\"\"
        limit=2**31 - 1
        for i in range(1,len(S)):
            if S[0]==\"0\" and i!=1:
                break
            for j in range(i+1,len(S)):
                if S[i]==\"0\" and j!=i+1:
                    break
                pre=int(S[:i])
                cur=int(S[i:j])
                ans=[pre,cur]
                k=j
                while k<len(S):
                    cur,pre=pre+cur,cur
                    if cur<=limit and str(cur)==S[k:k+len(str(cur))]:
                        ans.append(cur)
                        k=k+len(str(cur))
                    else:
                        break
                if k==len(S):
                    return ans
        return []
