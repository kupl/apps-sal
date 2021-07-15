# cook your dish here
t = int(input())
for i in range(t):
    s = input()
    s=s.lower()
    s=s.split()
    if "berhampore" in s and "serampore" in s:
        print("Both")
    elif "berhampore" in s:
        print("GCETTB")
    elif "serampore" in s:
        print("GCETTS")
    else:
        print("Others")

