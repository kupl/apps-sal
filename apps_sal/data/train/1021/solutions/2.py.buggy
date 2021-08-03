# cook your dish here
    n = int(input())
     
    l = list(map(int, input().split()))
     
    def conv(n):
    	i = 0
    	while n % 2 == 0:
    		i += 1
    		n /= 2
    	return (-n, i)
     
    l.sort(key=conv)
    print(*l)
