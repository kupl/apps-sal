from collections import deque
moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))

def knight(p1, p2):
    x, y = ord(p2[0])-97, int(p2[1])-1
    left, seen = deque([(ord(p1[0])-97, int(p1[1])-1, 0)]), set()
    while left:
        i, j, v = left.popleft()
        if i==x and j==y: return v
        if (i, j) in seen: continue
        seen.add((i, j))
        for a,b in moves:
            if 0 <= i+a < 8 and 0 <= j+b < 8:
                left.append((i+a, j+b, v+1))
