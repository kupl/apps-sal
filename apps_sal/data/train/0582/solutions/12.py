

def find_min(s,queries):

    stack = []

    balancing = [-1]*len(s)

    op = [-1]* len(s)

    last_opening = -1
    for i in range(len(s)-1,-1,-1):
        if s[i]==')':
            op[i] = last_opening
        else:
            last_opening = i


    for i in range(len(s)):
        if s[i]==')':
            if len(stack)!=0:
                balancing[stack[-1]] = i
                del stack[-1]
        else:
            stack.append(i)

    for query in queries:
        q = query-1
        if s[q]==')':
            if op[q]==-1:
                print(-1)
                continue
            else:
                q = op[q]
        if balancing[q]==-1:
            print(-1)
        else:
            print(balancing[q]+1)

T = int(input())
while T!=0:
    s = input()
    q = int(input())
    queries = [int(a) for a in input().split(" ")]
    find_min(s,queries)
    T-=1


