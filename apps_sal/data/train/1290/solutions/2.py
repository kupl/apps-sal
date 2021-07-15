# cook your dish here
t = int(input())
a = 0
while(t!=0):
 t = int(t/10)
 a += 1
if(a==1):
 print("1")
elif(a==2):
 print("2")
elif(a==3):
 print("3")
else:
 print("More than 3 digits")
