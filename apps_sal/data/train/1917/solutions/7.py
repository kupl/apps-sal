from collections import Counter
 
 def tokenizer(formula):
     result = []
     
     current_token = ""
     
     numbers = "0123456789"
     
     def append_current_token():
         nonlocal current_token, result
         
         if current_token:
             result.append(current_token)
             current_token = ""
     
     for char in formula:
         if char == "(":
             append_current_token()
             result.append(char)
             
         elif char == ")":
             append_current_token()
             result.append(char)
         
         elif char in numbers:
             if current_token and current_token[-1].isalpha():
                 append_current_token()
             
             current_token += char
             
         elif char.isalpha():
             if current_token and (current_token[-1] in numbers or char.isupper()) :
                 append_current_token()
             
             current_token += char
             
     
     append_current_token()
     
     return result
     
 
 class Solution:
     def countOfAtoms(self, formula):
         """
         :type formula: str
         :rtype: str
         """
         result = Counter()
         formula = tokenizer(formula)
         
         mult_stack = []
         mult = 1
         
         precedent_number = 1
         
         for token in formula[::-1]:
             if token.isdigit():
                 n = int(token)
                 precedent_number = n
             
             elif token.isalpha():
                 result[token] += mult * precedent_number
                 precedent_number = 1
             
             elif token == ")":
                 mult_stack.append(precedent_number)
                 mult *= precedent_number
                 precedent_number = 1
             
             elif token == "(":
                 n = mult_stack[-1]
                 mult_stack.pop()
                 
                 mult //= n
         
         
         
         str_result = []
         
         for token in sorted(result.keys()):
                 str_result.append(token + str(result[token]) if result[token] != 1 else token)
         
         return ''.join(str_result)
