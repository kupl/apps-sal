def f(n):
	if n<10:
		return n
	else:
		sum=0
		temp =n
		while(temp):
			sum+=temp%10
			temp/=10
		if(sum<10):
			return sum
		else:
			return f(sum)
t = int(input())
while(t):
    a,d,l,r =list(map(int, input().split()))
    ap =[]
    ap.append(f(a+(l-1)*d))
    for i in range(1,9):
        ap.append(f(ap[i-1]+d))
    temp = int((r-l+1)/9)
    ans=0
    for i in range(0,9):
        ans+=(ap[i]*temp)
    temp =(r-l+1)%9
    for i in range(0,temp):
        ans+=ap[i]
    print(ans)
    t-=1
