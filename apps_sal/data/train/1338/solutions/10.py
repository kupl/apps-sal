lis = list(map(float,input().split()))
n = int(lis[0])
for i in range(1,n*2,2):
    num = lis[i]
    power = 10**lis[i+1]
    #print(round(num*power,2))
    print("{0:.2f}".format(num*power)) 
