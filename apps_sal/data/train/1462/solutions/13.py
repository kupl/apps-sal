# cook your dish here
for i in range(0,int(input())):
    s=input()
    l=s.split(" ")
    p="berhampore"
    q="serampore"
    for i in range(0,len(l)):
        l[i]=l[i].lower()
    b=0
    s=0
    for i in l:
        if i == p:
            b +=1
        elif i == q:
            s+=1
    if b > 0 and s > 0 :
        print("Both")
    elif s > 0:
        print("GCETTS")
    elif b > 0:
        print("GCETTB")
    else:
        print("Others")
        

