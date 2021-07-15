# cook your dish here
try:
    t=int(input()) 
    for i in range(t):
        n=input() 
        n=n.lower()
        a="berhampore"
        b="serampore"
        if a in n:
            if b in n:
                print("Both")
            else:
                print("GCETTB")
        elif b in n:
            if a in n:
                print("Both")
            else:
                print("GCETTS")
        else:
            print("Others")
except Exception as e:
    pass
