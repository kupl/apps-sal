class Solution:
     flag = 0
     def reverse(self, x):
             if x < 0:
                 self.flag = 1
                 self.x = str(-x)
             else:
                 self.x = str(x)
 
             list1 = []
 
             for i in self.x:
                 if i != 0:
                     self.flag1 = 1
                 if self.flag1 == 1:
                     list1.insert(0,i)
             self.x = int("".join(list1))
 
             if self.flag == 1 :
                 self.x = -self.x
             if self.x <= 2147483647 and self.x >= -2147483648:
                 return self.x
             else:
                 return 0
