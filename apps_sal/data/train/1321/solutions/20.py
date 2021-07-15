for _ in range(int(input())):
    r=int(input())
    r-=1
    r=r*(r+1)*((2*r)+1)
    print(r//6)
