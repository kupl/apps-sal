try:
    for _ in range(int(input())):
        s=input().lower().split()
        a=0
        b=0
        if 'berhampore' in s:
            a=1
        if 'serampore' in s:
            b=1
        if a==1 and b==1:
            print("Both")
        elif a==1:
            print("GCETTB")
        elif b==1:
            print("GCETTS")
        else:
            print("Others")
except:
    pass

