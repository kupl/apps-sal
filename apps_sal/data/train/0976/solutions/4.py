n = int(input())
arr = list(map(int, input().split()))
b1 = b2 = maxb1 = maxb2 = b1pos = b2pos = 0
stacklen = 0
stack = []
currtoggle = 0
maxtoggle = 0
for i in range(n):
    if arr[i] == 1:
        if b1 == 0:
            b1pos = i
        b1 += 1
        if currtoggle == 0 or stack[-1] == 3:
            currtoggle += 1
        maxtoggle = max(currtoggle, maxtoggle)
        stack.append(1)
        stacklen += 1
    elif arr[i] == 2:
        b1 -= 1
        if b1 == 0 and i - b1pos + 1 > maxb1:
            maxb1 = i - b1pos + 1
        stack.pop()
        stacklen -= 1
        if stacklen == 0 or stack[-1] == 3:
            currtoggle -= 1
    elif arr[i] == 3:
        if b2 == 0:
            b2pos = i
        b2 += 1
        if currtoggle == 0 or stack[-1] == 1:
            currtoggle += 1
        maxtoggle = max(currtoggle, maxtoggle)
        stack.append(3)
        stacklen += 1
    else:
        b2 -= 1
        if b2 == 0 and i - b2pos + 1 > maxb2:
            maxb2 = i - b2pos + 1
        stack.pop()
        stacklen -= 1
        if stacklen == 0 or stack[-1] == 1:
            currtoggle -= 1
print(maxtoggle, maxb1, maxb2)
