class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans=0
        c=(2**31)-1
        def helper(pp,p,i,no):
            nonlocal ans
            if(i==len(S) and len(no)>=3):
                ans=no
                return True
            else:
                for j in range(i+1,len(S)+1):
                    ok=S[i:j]
                    if(ok[0]==\"0\" and len(S[i:j])>1):
                        continue
                    if(int(S[i:j])>c):
                        continue
                    let=int(S[i:j])
                    if(pp==-1):
                        if(helper(let,p,j,no+[let])):
                            return True
                    elif(p==-1):
                        if(helper(pp,let,j,no+[let])):
                            return True
                    else:
                        if(let==pp+p):
                            if(helper(p,let,j,no+[let])):
                                return True
            return False
        if(helper(-1,-1,0,[])==False):
            return []
        else:
            return ans
                
