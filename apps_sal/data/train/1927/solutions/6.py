class Solution:
     def asteroidCollision(self, asteroids):
         """
         :type asteroids: List[int]
         :rtype: List[int]
         """
         
         ret = []
         
         for val in asteroids:
             
             append_flag = True
             
             while len(ret) > 0:
                 
                 # both neg or pos
                 if val * ret[-1] > 0:
                     break
                     
                 if val > 0:
                     break
                 
                 # val fails, ignore it
                 if abs(val) < abs(ret[-1]):
                     append_flag = False
                     break
 
                 # [-5, 5]
                 if val + ret[-1] == 0:
                     ret.pop()
                     append_flag = False
                     break
                 
                 ret.pop()
                 
             if append_flag:
                 ret.append(val)
                 
         return ret
     

