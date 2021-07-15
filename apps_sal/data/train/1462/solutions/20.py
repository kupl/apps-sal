t=int(input())
for j in range(t):
    p=input()
    p=p.split(" ")
    flag="Others"
    for i in range(int(len(p))):
        if(p[i].lower()=="serampore"):
            if(flag=="Others"):
                flag="GCETTS"
            if(flag=="GCETTB"):
                flag="Both"
        if(p[i].lower()=="berhampore"):
            if(flag=="Others"):
                flag="GCETTB"
            if(flag=="GCETTS"):
                flag="Both"
    print(flag)

