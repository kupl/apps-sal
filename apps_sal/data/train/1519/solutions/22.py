t = int(input())
for w in range(0,t):
    x = int(input())
    x = x - 1
    for i in range(1,60):
        if x<(2**i):
            print(2**i)
            break
