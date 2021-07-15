def mouth_size(animal): 
  result = ""
  animal_recase = animal.lower() #to make all forms of alligator 'readable'
  if animal_recase == "alligator":
      result = "small"
  else:
      result = "wide"
  return result   
