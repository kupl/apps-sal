a,b,c,d = list(map(int , input().split()))

if(a*d == c*b or a*c == d*b or b*d == c*a or b*c == d*a):
 print("Possible")
elif(a*d == b*c or a*b ==d*c or c*d == b*a or c*b == d*a):
 print("Possible")
elif(a*c == b*d or a*b == c*d or d*c == b*a or d*b == c*a):
 print("Possible")
else:
 print("Impossible") 
