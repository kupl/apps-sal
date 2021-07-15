import re
def string_to_array(s):

   # your code here
   return re.split(r'[;,\s]\s*', s) 
