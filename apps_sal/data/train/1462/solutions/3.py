# cook your dish here
t = int(input())
for _ in range(t):
    s = input()
    ss = s.lower()
    a = 'berhampore'
    b = 'serampore'
    if a in ss and b in ss:
        print("Both")
    elif a in ss:
        print("GCETTB")
    elif b in ss:
        print("GCETTS")
    else:
        print("Others")
