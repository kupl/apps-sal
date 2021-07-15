t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    data = list(map(int, input().split()))
    stack = []
    for i in data:
        if not stack:
            stack.append(i)
        else:
            while stack and stack[-1] > i:
                c += 1
                stack.pop()
            stack.append(i)
    print(c)
