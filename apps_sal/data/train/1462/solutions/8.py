try:
    t = int(input())
    for _ in range(t):
        x = input().lower()
        if("berhampore" in x and "serampore" in x):
            print("Both")
        elif("berhampore" in x):
            print("GCETTB")
        elif("serampore" in x):
            print("GCETTS")
        else:
            print("Others")
except:
    pass
