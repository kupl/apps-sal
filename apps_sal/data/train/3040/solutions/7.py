def candies(s):
   if len(s)<2:
     return -1
   else:
     return(sum([max(s)-i for i in s]))
