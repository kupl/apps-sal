def xor(a,b):

   result = True
   
   if a==True and b==True:
      result=False
   elif (a == True and b == False) or   (b == True and a ==False):
      result=True
   elif a==False and b==False:
      result=False 
      
   return result   
