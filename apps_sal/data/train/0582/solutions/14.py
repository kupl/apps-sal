# from mymodule import input
t = int(input())
for _ in range(t):
    s = input().strip()
    li, stk, tmp = [-1] * len(s), [], []
    for i in range(len(s)):
        if len(stk):
            if s[i] == '(':
                while len(tmp):
                    stk.append(tmp.pop())
                stk.append(i)
            elif s[stk[-1]] == '(':
                li[stk[-1]] = i
                v = stk.pop()
                while len(stk) != 0:
                    if s[stk[-1]] == ')':
                        li[stk[-1]] = v
                        stk.pop()
                    else:
                        break
                tmp.append(i)
            else:
                stk.append(i)
            pass
        elif s[i] == '(':
            while len(tmp) != 0:
                stk.append(tmp.pop())
            stk.append(i)
        else:
            stk.append(i)
    # for i in tmp:
    #     li[i] = len(s)
    # print(li,stk)
    q = int(input())
    for i in map(int, input().split()):
        ind = i - 1
        while li[ind] != -1 and s[li[ind]] != ')':
            ind = li[ind]
        if li[ind] != -1:
            print(li[ind] + 1)
        else:
            print(-1)
