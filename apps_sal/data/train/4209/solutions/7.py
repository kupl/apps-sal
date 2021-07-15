from collections import deque

def largest_rect(a):
    areas, stack, a = [], deque(), a + [0]
    for i, x in enumerate(a):
        j = i
        while len(stack) > 0 and x <= stack[-1][1]:
            j, h = stack.pop()
            areas.append((i-j) * h)
        stack.append((j, x))
    return max(areas or [0])
