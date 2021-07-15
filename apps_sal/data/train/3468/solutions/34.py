from collections import deque

def scramble(s1,s2):
    s1 = deque(sorted(s1))
    s2 = sorted(s2)
    for letter in s2:
        if len(s1) == 0:
            return False
        while len(s1):
            next_letter = s1.popleft()
            if next_letter == letter:
                break
            if next_letter > letter:
                return False
    return True
