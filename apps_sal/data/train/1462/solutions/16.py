T = int(input())
for i in range(T):
    s = input()
    s = s.lower()
    l = s.split()
    f1 = 0
    f2 = 0
    for j in l:
        if (j == "serampore"):
            f1 = 1
        elif (j == "berhampore"):
            f2 = 1
    if (f1 == 1 and f2 == 1):
        print("Both")
    elif (f1 == 1 and f2 == 0):
        print("GCETTS")
    elif (f1 == 0 and f2 == 1):
        print("GCETTB")
    else:
        print("Others")
