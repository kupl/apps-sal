# cook your dish here
for _ in range(int(input())):
    N=int(input())
    seq=N//2
    if(N==1):
        print(1)
        print(1,1)
    elif(N==2):
        print(seq)
        print(2,1,2)
    elif(N%2!=0):
        print(seq)
        for i in range(1,N+1,2):
            if(i==1):
                print(3,1,i+1,i+2)
            elif(i>=4):
                print(2,i-1,i)
    else:
        print(seq)
        for i in range(1,N+1,2):
            if(i==1):
                print(2,1,i+1)
            elif(i>=3):
                print(2,i,i+1)
