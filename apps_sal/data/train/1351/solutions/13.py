# cook your dish here
t = int(input())
while(t):
    n = int(input())
    A = list(map(int,input().strip().split(" ")))
    A = set(A)
    # A = list(A)
    m = max(A)
    B = [0]*(n)
    for ele in A:
        if(B[ele] == 0):
            B[ele]=1
        else:
            pass
    for j  in range(len(B)):
        if( B[j]==0):
            print(0,end=" ")
        else:
            print(j,end=" ")
    print()
    
        
    t = t-1

