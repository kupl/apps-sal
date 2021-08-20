import collections
import sys
(n, q) = map(int, input().split())
hash = {}
deque = collections.deque()
messageNumber = 1
unread = 0
L = []
for i in range(q):
    (c, x) = map(int, input().split())
    if c == 1:
        if x not in hash:
            hash[x] = set()
        hash[x].add(messageNumber)
        deque.append((x, messageNumber))
        messageNumber += 1
        unread += 1
    elif c == 2:
        if x in hash:
            xUnread = len(hash[x])
            hash[x] = set()
            unread -= xUnread
    else:
        t = x
        read = 0
        while len(deque) != 0 and deque[0][1] <= t:
            (app, message) = deque.popleft()
            if message in hash[app]:
                read += 1
                hash[app].remove(message)
        unread -= read
    L.append(unread)
print('\n'.join(map(str, L)))
