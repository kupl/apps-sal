for _ in range(int(input())):
    s = input()
    s1 = s.lower()
    if "berhampore" in s1:
        if "serampore" in s1:
            print("Both")
        else:
            print("GCETTB")
    elif "serampore" in s1:
        print("GCETTS")
    else:
        print("Others")
