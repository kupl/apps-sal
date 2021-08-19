# cook your dish here

# cook your dish here


t = int(input())
while t:
    t -= 1
    c = 0
    ar = [int(i) for i in input().strip().split()]
    for i in range(1, 16):
        b = bin(i)[2:].zfill(4)
        s = 0
        for i in range(4):
            if b[i] == '1':
                s += ar[i]

        if(s == 0):
            c = 1
            break

    print("Yes" if c == 1 else "No")
