arr=[0]*10000
for i in range(1,10000):
    arr[i]=arr[i-1]+(i*i)

t=int(input())
for i in range(t):
    n=int(input())
    print(arr[n-1])
