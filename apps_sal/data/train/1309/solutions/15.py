for u in range(int(input().strip())):
    n = int(input().strip())
    for i in range(n):
        for space in range(1,i+1):
            print('*',end="")
        for j in range(n-i):
            print(n-i-j,end="")
        
        print()
