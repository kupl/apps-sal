t = int(input())
for i in range(t):
    m, n = input().split()
    if(int(n) < 9):
        print(0, 0)
    elif(int(n) > 9):
        print(int(m) * (len(n) - 1), int(m))
    else:
        print(int(m), int(m))
