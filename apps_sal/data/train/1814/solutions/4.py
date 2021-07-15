class Solution:
     def exclusiveTime(self, n, logs):
         """
         :type n: int
         :type logs: List[str]
         :rtype: List[int]
         """
         s=[]
         a=[0]*n
         pop=False
         for log in logs:
             l=log.split(':')
             if l[1]=='start' and len(s)>0:
                 a[s[-1]]+=int(l[2])-prev
                 s.append(int(l[0]))
                 prev=int(l[2])
                 pop=False
             elif l[1]=='start':
                 s.append(int(l[0]))
                 pop=False
                 prev=int(l[2])
             elif l[1]=='end':
                 
                 a[s[-1]]+=int(l[2])-prev+1
                 s.pop()
                 pop=True
             
                 prev=int(l[2])+1
         return a
