def reverse_list(l):
  'return a list with the reverse order of l'
  result = []
  counter = 0
  while counter < len(l):
      result.append( l[ -1 - counter]  )
      counter +=1
  return result    
  

