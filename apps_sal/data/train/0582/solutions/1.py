# cook your dish here
T = int(input())
for _ in range(T):
    s = input()
    _ = input()
    stack = []
    nextOpen = [-1 for _ in range(len(s))]
    closing = [-1 for _ in range(len(s))]
    nextO = len(s) + 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            nextO = i
            if stack:
                closing[i] = stack.pop()
        else:
            stack.append(i)
        nextOpen[i] = nextO

    for t in map(int, input().split()):
        t -= 1
        t = nextOpen[t]
        if t < len(s):
            res = closing[t]
            print(res + 1 if res >= 0 else -1)
        else:
            print(-1)
