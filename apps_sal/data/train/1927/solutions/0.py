class Solution:
     def asteroidCollision(self, asteroids):
         """
         :type asteroids: List[int]
         :rtype: List[int]
         """
         l=len(asteroids)
         if l<2:
             return asteroids
         ans=[]
         stack=[]
         for a in asteroids:
             if a>0:
                 stack.append(a)
             else:
                 a=-a
                 equal_flag=False
                 while stack:
                     cur=stack.pop()                  
                     if cur==a:
                         equal_flag=True
                         break
                     elif cur>a:
                         stack.append(cur)
                         break              
                 if equal_flag:
                     continue            
                 if not stack:
                     ans.append(-a)
         return ans+stack
             

