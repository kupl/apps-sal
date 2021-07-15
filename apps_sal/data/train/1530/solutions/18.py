#Pattern J
T = int(input())

for t in range(T):
    N = int(input())
    num = 1
    for i in range(N):
        sol = ""
        for j in range(i+1):
            sol = str(num) + sol
            num+=1
        print(sol)
