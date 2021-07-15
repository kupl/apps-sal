MOD = 1000000007
st,n,t,mp=input(),int(input()),[],{}

t.append(['',st])

for i in range(10):
	mp[str(i)]=(10,i)

for i in range(n):
	t.append(input().split("->"))

for i in range(n,-1,-1):
	a,b=1,0
	for j in t[i][1]:
		a,b=a*mp[j][0]%MOD,(b*mp[j][0]+mp[j][1])%MOD
	mp[t[i][0]]= a,b

print(mp[''][1])




# Made By Mostafa_Khaled

