T=int(input())
for t in range(T):
    K=int(input())
    if K==0:
        print("0")
    else:
        K=K-1
        output=K*(K+1)*(2*K+1)/6
        print(int(output))
