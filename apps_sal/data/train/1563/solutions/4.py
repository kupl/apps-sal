t = int(input(""));
for i in range(t):
 s1,s2 = (input("").split());
 s1=str(int(s1))
 s2=str(int(s2))
 s1 = s1[::-1];
 s2 = s2[::-1];
 sum = int(s1) + int(s2) ;
 sum = str(sum)
 sum = sum[::-1];
 print(int(sum))
