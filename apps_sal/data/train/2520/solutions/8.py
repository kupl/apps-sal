class Solution:
     def reverse(self, x):
         """
         :type x: int
         :rtype: int
         """
         if x.bit_length()>32 :
     
             print("wrong");
         else:
             number = [];
             digit_num = [];
             new_num = 0;
       
             error = abs(x);
             for i in range(len(str(abs(x)))):
                 if not number:
                     digit = abs(x)//10**(len(str(abs(x)))-1);    
                     number.append(str(digit));
                     digit_num.append(digit);
                 else:
                     error = error - digit_num[i-1]*10**(len(str(abs(x)))-i);
                     digit = error//10**(len(str(abs(x)))-1-i);                  
                     number.append(str(digit));
                     digit_num.append(digit);
                     
             number.reverse();
           
             while(int(number[0])==0 and len(number)>1):
                 del number[0];
                 
             for i in range(len(number)):
                 new_num = new_num + int(number[i])*10**(len(number)-i-1);
             if new_num.bit_length()>=32:
                 return 0;
             
             if x<0:
                 new_num = -new_num;
             return new_num;
