for i in range(int(input())):
 userstring = input()
 count = userstring.count('01') + userstring.count('10')
 if userstring[-1]!=userstring[0] :
  count = count +1
 if count <=2 :
  print("uniform")
 else :
  print("non-uniform")

