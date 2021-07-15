input()

a=list(map(int,input().split()))

cnt=0

while a:

 i=a.index(a.pop(0))

 cnt+=i

 a.pop(i)

print(cnt)



# Made By Mostafa_Khaled

