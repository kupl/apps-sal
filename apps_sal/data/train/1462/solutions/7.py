t = int(input())
for i in range(t):
    a = input()
    a = a.upper()
    b = a.find("BERHAMPORE", 0, len(a))
    c = a.find("SERAMPORE", 0, len(a))
    if b != -1 and c == -1:
        print("GCETTB")
    elif b == -1 and c != -1:
        print("GCETTS")
    elif b != -1 and c != -1:
        print("Both")
    elif b == -1 and c == -1:
        print("Others")
