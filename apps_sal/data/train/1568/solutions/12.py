for i in range(int(input())):
    count = 0
    n = int(input())
    a = list(map(int,input().split()))
    for j in a:
    	if (2*j>=n):
            count+=1
    print(count)
