class Solution:
     def countOfAtoms(self, formula):
         """
         :type formula: str
         :rtype: str
         """
         formula+=' '
         stack,i=[{}],0
         while i<len(formula):
             if formula[i]>='A' and formula[i]<='Z':
                 j=i+1
                 while formula[j]>='a' and formula[j]<='z':
                     j+=1
                 k=j
                 while formula[k]>='0' and formula[k]<='9':
                     k+=1
                 t=1 if k==j else int(formula[j:k])
                 stack[-1][formula[i:j]]=stack[-1].get(formula[i:j],0)+t
                 i=k
             elif formula[i]=='(':
                 stack.append({})
                 i+=1
             elif formula[i]==')':
                 j=i+1
                 while formula[j]>='0' and formula[j]<='9':
                     j+=1
                 t=1 if j==i+1 else int(formula[i+1:j])
                 for x in stack[-1]:
                     stack[-2][x]=stack[-2].get(x,0)+stack[-1][x]*t
                 stack.pop()
                 i=j
             else:
                 i+=1
         a,s=sorted(stack[-1].keys()),''
         for x in a:
             s+=x if stack[-1][x]==1 else x+str(stack[-1][x])
         return s
