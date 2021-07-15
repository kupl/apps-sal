class Solution(object):
     loc=0
     lastloc=-1
     f=''
     def getNext(self,formular,locked=False):
         stype=0 # 0:null, 1:numeric, 2/20: Elem, 3: parenthesis
         ret=0
         if self.loc==self.lastloc: return (0,0)
         i=self.loc
         while i <len(formular):
             if stype in (0,1) and  formular[i].isnumeric():
                 ret=int(formular[i])+ret*10
                 stype=1
             elif stype==0 and formular[i].isupper():
                 stype=20
                 ret=formular[i]
             elif stype in (20,2) and formular[i].islower():
                 stype=2
                 ret+=formular[i]
             elif stype==0 and formular[i] in "()":
                 stype=3+"()".index(formular[i])
                 ret=formular[i]
             else: break
             i+=1
         if not locked:
             self.lastloc=self.loc
             self.loc=i
         return (stype,ret)
     
     def countOfAtoms(self, formula):
         stk=[]
         cnt={}
         r=''
         self.loc=0
         n=self.getNext(formula)
         while n!=(0,0):
             if n[0] in (2,3,20):
                 stk.append([n[1],1])
             elif n[0]==1:
                 stk[-1][1]=n[1]
             elif n[0]==4:
                 time=1
                 i=-1
                 if self.getNext(formula,True)[0]==1:
                     time=self.getNext(formula)[1]
                 while stk[i][0]!='(':
                     stk[i][1]*=time
                     i-=1
                 stk[i][0]='$'
             n=self.getNext(formula)
         while any(stk):
             n=stk.pop()
             if n[0]!='$':
                 cnt[n[0]]=cnt.get(n[0],0)+n[1]
         for i in sorted(cnt.keys()):
             r+="%s%d"%(i,cnt[i]) if cnt[i]>1 else i
         return r
