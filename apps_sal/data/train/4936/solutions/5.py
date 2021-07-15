from collections import deque

def reverse(lst):
    cheat = deque(lst)
    cheat.reverse()
    return list(cheat)
