for _ in range(int(input())):
 input_1 = str(input())
 str1 = "010"
 str2 = "101"
 
 if input_1.find(str1) == -1 and input_1.find(str2)== -1:
  print("Bad")
 else: 
  print("Good")
