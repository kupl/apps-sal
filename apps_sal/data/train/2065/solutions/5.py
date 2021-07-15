3
n1 = []
n1 = input("").split(" ")
n = int (n1[0])
k= int(n1[1])
x= int (0)
y= int(-1)
z = int (0)


breakc = int(0)
addc = int(0)
x = []
f =int(0)
for i in range(0,k):
	x=input("").split(" ")
	y = -1
	if f != 1:
		for j in range(1,int(x[0])+1):
			z=int(x[j])
			if z==1:
				y = 1
				for k in range(j+1, int(x[0])+1):
					z=int(x[k])
					if z == (y+1):
						addc +=1
						y =z
					else:
						f = 1
					if k == int(x[0]):
						f = 1
					if f == 1:
						x[0] = int(x[0]) - addc
						
						break
			
				
					
	breakc += int(x[0]) - 1


print(breakc + (n - addc) - 1)

