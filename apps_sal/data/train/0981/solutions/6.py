t = eval(input())
while t > 0:
    t -= 1
    n = eval(input())
    str = input()
    inp = str.split()
    inp = list(map(int, inp))
    inp.sort()
    smallest = abs(inp[0] - inp[1])
    for i in range(1, n - 1):
        temp = abs(inp[i] - inp[i + 1])
        if temp < smallest:
            smallest = temp
    print(smallest)
