t = int(input())
for _ in range(t):
    s = input()
    s = list(s)
    n = len(s)
    answer = []
    stack = []
    stack2 = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ')':
            if answer == []:
                answer = [-1]
                stack2.append(i)
                stack.append(')')
                continue
            stack2.append(i)
            answer.append(answer[-1])
            stack.append(')')
        elif stack2 == []:
            answer.append(-1)
            stack.append('(')
        else:
            stack.pop()
            e = stack2[-1]
            stack2.pop()
            answer.append(e + 1)
    answer.reverse()
    q = int(input())
    W = list(map(int, input().split()))
    for i in range(q):
        w = W[i]
        print(answer[w - 1])
