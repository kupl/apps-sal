n = int(input())
a = [int(n) for n in input().split()]
stack = []
maxx = 0
i = 0
while i < n:
    if not stack or a[i] < stack[-1]:
        stack.append(a[i])
        i += 1
    else:
        maxx = max(stack[-1] ^ a[i], maxx)
        temp = stack.pop()
        if stack:
            maxx = max(stack[-1] ^ temp, maxx)
while len(stack) != 1:
    temp = stack.pop()
    maxx = max(temp ^ stack[-1], maxx)
print(maxx)
