def Check(ram,shyam):
    for i in shyam:
        if i not in ram:
            return False
    return True

for _ in range(int(input())):
    tR = int(input())
    Tr = list(map(int,input().split()))
    dR = int(input())
    Dr = list(map(int,input().split()))
    tS = int(input())
    Ts = list(map(int,input().split()))
    dS = int(input())
    Ds = list(map(int,input().split()))
    truthCheck = Check(Tr,Ts)
    dareCheck = Check(Dr,Ds)
    if ( truthCheck and dareCheck ):
        print("yes")
    else:
        print("no")
    
