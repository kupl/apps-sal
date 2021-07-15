# cook your dish here
# cook your dish here
def solve():
    n = int(input())
    #n,m = input().split()
    #n = int(n)
    #m = int(m)
    #s = input()
    #a = list(map(int, input().split()))
    k=n//2
    for i in range(n):
        j=0
        if i<=k : z=i
        else: z=n-i-1
        while j!=z :
            print(" ",end="")
            j+=1
        print("*")
        
            
    
    
def __starting_point():
    T = int(input())
    for i in range(T):
        #a = solve()
        #n = len(a)
        #for i in range(n):
         #   if i==n-1 : print(a[i])
          #  else: print(a[i],end=" ")
        (solve())
__starting_point()
