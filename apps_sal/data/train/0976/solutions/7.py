t = int(input())
s = ''
g = []
g = list(map(int, input().split()))
for ele in g:
    if ele == 1:
        s += '('
    elif ele == 2:
        s += ')'
    elif ele == 3:
        s += '['
    else:
        s += ']'
stack = []
deptho = 0
if len(s) > 0:
    deptho = 1
d = {}
d[0] = deptho
d[1] = 0
d[2] = 0
stack = []
depth = []
for i in range(t):
    if len(stack) == 0 and (s[i] == '(' or s[i] == '['):
        stack.append(s[i])
        depth.append(1)
    elif s[i] == '(' and stack[-1] == '[' or (s[i] == '[' and stack[-1] == '('):
        stack.append(s[i])
        depth.append(depth[-1] + 1)
    elif s[i] == '(' or s[i] == '[':
        stack.append(s[i])
        depth.append(depth[-1])
    deptho = max(deptho, depth[-1])
    if s[i] == ')' or s[i] == ']':
        stack.pop()
        depth.pop()
d[0] = deptho
p_char = 0
sq_char = 0
max_sq_char = 0
max_p_char = 0
p_depth = 0
sq_depth = 0
for i in range(t):
    if s[i] == '(':
        p_depth += 1
    if s[i] == '[':
        sq_depth += 1
    if p_depth:
        p_char += 1
    if sq_depth:
        sq_char += 1
    max_sq_char = max(max_sq_char, sq_char)
    max_p_char = max(max_p_char, p_char)
    if s[i] == ')':
        p_depth -= 1
    if s[i] == ']':
        sq_depth -= 1
    if p_depth == 0:
        p_char = 0
    if sq_depth == 0:
        sq_char = 0
d[1] = max_p_char
d[2] = max_sq_char
print(d[0], d[1], d[2])
