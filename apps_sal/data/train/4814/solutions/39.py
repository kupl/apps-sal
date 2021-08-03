import collections


def is_palindrome(s):
    deq = collections.deque([c for c in s.lower()])
    palFlag = True
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return palFlag
