for _ in range(int(input())):
    n=int(input())
    rule=[]
    ci=""
    pi=""
    for _ in range(n):
        c,p=input().split()
        ci+=c
        pi+=p
    trans=str.maketrans(ci,pi)
    s=input()
    s=s.translate(trans)
    s="".join(s)
    dot = s.find(".")
    if dot!=-1:
        s=s.strip("0").rstrip(".")
    else:
        s=s.lstrip("0")
        
    if s=="":
        print(0)
    else:
        print(s)
