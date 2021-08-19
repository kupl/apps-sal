
import sys
import collections
n, q = list(map(int, input().split()))

# Key: app number, value: list of indexes in the arr
M = collections.defaultdict(collections.deque)

# arr = []
Q = collections.deque()
n = 0
s = 0
m = 0
L = []
for i in range(q):
    c, x = list(map(int, input().split()))

    if c == 1:
        # if x not in M:
        #   M[x] = collections.deque()
        # M[x] = set()

        # M[x].add(n)
        M[x].append(n)
        Q.append(x)

        n += 1
        s += 1

        # print("case 1")

    elif c == 2:
        y = M.get(x)
        if y:
            s -= len(y)

            del M[x]

        # print("case 2")

    else:
        while x > m:
            z = Q.popleft()
            y = M.get(z)
            if y and y[0] < x:
                s -= 1
                y.popleft()

                if not y:
                    del M[z]
                # M[app].remove(message)

            m += 1
        # print("case 3")
    L.append(s)
sys.stdout.write('\n'.join(map(str, L)))

# for i in range(q):
#   c, x = map(int, input().split())

#   if c == 1:
#     if x not in hash:
#       hash[x] = collections.deque()
#       # hash[x] = set()

#     # hash[x].add(messageNumber)
#     hash[x].append(messageNumber)
#     deque.append((x, messageNumber))

#     messageNumber += 1
#     unread += 1

#     # print("case 1")
#     print(unread)

#   elif c == 2:
#     if x in hash:
#       xUnread = len(hash[x])
#       hash[x] = set()
#       unread -= xUnread
#     # print("case 2")
#     print(unread)

#   else:
#     t = x
#     read = 0
#     while len(deque) != 0 and deque[0][1] <= t:
#       app, message = deque.popleft()

#       if message in hash[app]:
#         read += 1
#         hash[app].remove(message)

#     unread -= read

#     # print("case 3")
#     print(unread)
