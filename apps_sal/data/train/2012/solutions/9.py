n=int(input())
if n==1:
	print (1)
	return
if n%4>1:
	print (-1)
	return
ans=[-1]*n
left=n
start=n-2
nums=1
nume=n
while left>=4:
	ans[start]=nums
	ans[nums-1]=nums+1
	ans[nums]=nume
	ans[nume-1]=nume-1
	start-=2
	nums+=2
	nume-=2
	left-=4
	# print (ans)
if left==1:
	ans[start+1]=start+2
print (*ans)
