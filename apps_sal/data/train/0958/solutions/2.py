testcases=int(input())
for i in range(testcases):
    n=int(input())
    j=n-1
    space=-1
    for i in range(1, n):
        print(' '*j, end="")
        print("*", end="")
        print(" "*(2*space+1), end="")
        if(i!=1):
            print("*", end="")
        j-=1
        space+=1
        print()
    print("*"*(2*n-1), end="")
    print()
