import collections
import sys

n, q = list(map(int, input().split()))
# Key: app number, value: list of indexes in the arr
hash = {}

# arr = []
deque = collections.deque()
messageNumber = 1
unread = 0
L = []

for i in range(q):
  c, x = list(map(int, input().split()))

  if c == 1:
    if x not in hash:
      hash[x] = set()

    hash[x].add(messageNumber)
    deque.append((x, messageNumber))

    messageNumber += 1
    unread += 1

    # print("case 1")
    # print(unread)

  elif c == 2:
    if x in hash:
      xUnread = len(hash[x])
      hash[x] = set()
      unread -= xUnread
    # print("case 2")
    # print(unread)

  else:
    t = x
    read = 0
    while len(deque) != 0 and deque[0][1] <= t:
      app, message = deque.popleft()

      if message in hash[app]:
        read += 1
        hash[app].remove(message)

    unread -= read

    # print("case 3")
    # print(unread)
  L.append(unread)
sys.stdout.write('\n'.join(map(str, L)))

