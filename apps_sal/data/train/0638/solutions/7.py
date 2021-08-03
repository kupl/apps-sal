t = int(input())
for i in range(t):
    print('Case ', (i + 1), ": ", sep='')
    inp = input().split()
    inp[0] = int(inp[0])
    inp[1] = int(inp[1])
    for j in range(inp[1]):
        length = len(input())
        if inp[0] == length:
            print("1")
        elif inp[0] < length:
            print("0")
        else:
            ans = ((inp[0] - length + 1) * (pow(26, inp[0] - length, 1000000007))) % 1000000007
            print(ans)
