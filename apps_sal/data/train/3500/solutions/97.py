def remove_exclamation_marks(s):
   print(s)
   
   answer = s.translate({ord('!'): None})
   return answer
