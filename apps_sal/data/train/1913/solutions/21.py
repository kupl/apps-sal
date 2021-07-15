class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        stack=[]
        find=-1
        for i in range(1,len(A)):
            if A[i]<A[i-1]:
                find=i-1
                break
        if find ==-1:
            return A
        j=find
        ind=[]
        3210
        while j<len(A):
            
            if len(stack)==0:
                stack.append(j)
                j+=1
                continue
            if A[j]<A[stack[-1]]:
                if len(stack)==2:
                    a=stack[-1]
                    stack=[a,j]
                else:
                    stack.append(j)
                j+=1
                continue
            else:
                if len(stack)==2:
                    ind=[stack[0],stack[1]]
                stack.pop()
        
        if len(stack)==2:
            A[stack[0]],A[stack[1]]=A[stack[1]],A[stack[0]]
            return A
        if len(ind)==2:
            A[ind[0]],A[ind[1]]=A[ind[1]],A[ind[0]]
            return A
        return A
        if len(stack)==0 and len(ind)==0:
            return A

