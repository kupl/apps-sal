t = int(input())
for z in range(t):
    N = map(str, input())
    s = ''
    for i in N:
        s += str(int(i) - 2)
    print(s)
