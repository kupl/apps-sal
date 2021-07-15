class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        def helper(a, i, j, cur_ans):
            if S[i]=='0' and j!=i+1:
                cur_ans=[]
                return False
            if a>2**31-1:
                return False
            b=int(S[i:j])
            c=a+b
            if b>2**31-1 or c>2**31-1:
                return False
            c_s=str(c)
            if c_s==S[j:j+len(c_s)]:
                k=j+len(c_s)
                cur_ans.append(c)
                if k==len(S):
                    return True
                if helper(b, j, k, cur_ans):
                    return True
                else:
                    cur_ans=[]
                    return False
            cur_ans=[]
            return False
        if len(S)==0:
            return []
        
        for i in range(1, len(S)):
            
            if i>1 and S[0]=='0':
                break
            a=int(S[:i])
            for j in range(i+1, len(S)):
                cur_ans=[a, int(S[i:j])]
                if helper(a, i, j, cur_ans):
                    return cur_ans
        
        return []
