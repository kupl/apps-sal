# cook your dish here
t =int(input())
while t>0:
    N,K = map(int,input().split())
    std_pow = list(map(int,input().split()))
    max_sum = sum(std_pow[:K])
    k12 = max_sum
    z=0
    # print(max_sum)
    for i in range(K,N):
        # print("index is "+str(i))
        k12 = k12 + std_pow[i] - ((std_pow[z]))
        # print(k12)
        z=z+1
        if k12>max_sum:
            max_sum=k12
            
    print(max_sum)        
    t=t-1
