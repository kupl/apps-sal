def create_phone_number(n):
  d='('
  #for loop to go through the array
  for i in range(len(n)):
  #get the first part of the final string
      if i<3:
          d=d+str(n[i])
          if i==2:
              d=d+') '
  #get the middle part of the final string
      elif i>=3 and i<6:
         
          d=d+str(n[i])
          if i==5:
              d=d+'-'
  #get the last 4 string members of the final string
      elif i>=6 and i<10:
   
          d=d+str(n[i])
  # return the entire string        
  return d
      

