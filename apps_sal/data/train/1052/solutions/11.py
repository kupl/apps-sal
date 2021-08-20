import queue


def digitsum(a):
    lo = 0
    s = str(a)
    for i in s:
        lo += int(i)
    return lo


for _ in range(int(input())):
    (min1, pos) = (1000000, -10)
    track = queue.Queue(100000)
    (n, d) = map(int, input().split())
    i = 0
    track.put([n, 0])
    while i < 100000 and track.empty() != True:
        (a, b) = track.get()
        if min1 > a:
            min1 = a
            pos = b
        if a > 9:
            track.put([digitsum(a), b + 1])
        track.put([a + d, b + 1])
        i += 1
    print(min1, pos)
