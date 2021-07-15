list1=[]
for i in range(int(input())):
 list1.append(list(map(int,input().split())))
apple=[]
orange=[]
mango=[]
for i in range(len(list1)):
 apples=list1[i][0]+list1[i][2]-list1[i][1]
 apple.append(apples/2)
 mango.append(list1[i][0]-apple[i])
 orange.append(list1[i][2]-apple[i])
for i in range(len(list1)):
 print(int(apple[i]),int(mango[i]),int(orange[i]))

