from sys import stdin, stdout
t = int(stdin.readline())
while(t):
    t -= 1
    string = str(stdin.readline())
    q = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    pos = 0
    l = {}
    stack = []
    pos = -1
    for j in range(len(string) - 1, -1, -1):
        if(string[j] == ')'):
            stack.append(j)
            l[j + 1] = pos
        elif(string[j] == '('):
            if(len(stack) >= 1):
                l[j + 1] = stack[-1] + 1
                pos = l[j + 1]
                stack.pop()
            else:
                l[j + 1] = -1
                pos = l[j + 1]
    for item in a:
        print(l[item])
