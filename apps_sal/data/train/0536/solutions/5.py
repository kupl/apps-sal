t = input()
t = int(t)
while t != 0:
    inp = input().split(' ')
    inp = [int(x) for x in inp]
    print(int(inp[1] / inp[0]))
    t -= 1
